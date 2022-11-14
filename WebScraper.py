# Alan Li, Imperial College London
# AICore 2022, all rights reserved

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import chromedriver_binary

class Scraper:
    '''
    Scrapes chosen data from the given website.
    Note: This requires the webdriver for the browser you are using to be in the PATH.
    To test this, launch cmd/bash and type "chromedriver" / "geckodriver" and
    see if it can be started successfully.

    Args:
    ----------
    URL: str
    The URL of the website to be scraped.
    driver: webdriver
    The browser used to load the webpage.
    data_dir: str
    The relative path of the directory in which the data will be stored.
    headless: bool
    When True, the script will run headlessly (to save GPU & CPU when scraping)
    '''

    def __init__(self, URL: str, driver: webdriver.Chrome = webdriver.Chrome(), data_dir: str = 'raw_data', headless: bool = False):
        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=chrome_options)
        else:
            self.driver = driver
        self.URL = URL
        self.data_dir = data_dir
        # If directory not found, create one
        if os.path.exists(data_dir) == False:
            os.mkdir(data_dir)
        self.driver.get(self.URL)

    def click_element(self, xpath: str):
        '''
        Find an element by Xpath and click on it.
        
        Parameters
        ----------
        xpath: str
            The Xpath of the element
        '''
        try:
            button = self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            print("Button not found!")
        button.click()

    def _load_and_accept_cookies(self, container_path: str, button_path: str):
        '''        
        Loads the page and waits for the container to appear. When the container appears, it
        clicks on the accept button.
        If the accept cookies button is not found, the code proceeds.
        
        Parameters
        ----------
        container_path: str
            The Xpath of the cookies consent container
        button_path: str
            The Xpath of the "Accept" button
        
        '''
        self.driver.get(self.URL) # Load the page
        delay = 6
        try:
            # Wait for the container to appear
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, container_path)))
            self.click_element(self, button_path)
        except TimeoutException:
            print("Time out: Failed to find the accept cookies button")
            print("Moving on...")
