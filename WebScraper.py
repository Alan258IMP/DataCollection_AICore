# Alan Li, Imperial College London
# AICore 2022, all rights reserved

import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import urllib
import requests
import os
import numpy

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

    Attributes:
    ----------

    Methods:
    -------
    '''

    def __init__(self, URL: str, driver: webdriver.Chrome, data_dir: str, headless: bool = False):
        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--window-size=1600,900")
            chrome_options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        else:
            self.driver = driver
        self.URL = URL
        self.data_dir = data_dir
        # If directory not found, create one
        if os.path.exists() == False:
            os.mkdir(data_dir)
        # Accept cookies upon initialization
        self._load_and_accept_cookies()

    def click_button(self, xpath: str):
        # Find an element and click on it
        try:
            button = self.driver.find_element(By.XPATH, xpath)
            button.click()
        except TimeoutException:
            print("TimeoutException: Button not found")

    def _load_and_accept_cookies(self, container_path: str, button_path: str):
        # XPaths of the container and the accept button needs to be given: Is it a bad practice?
        # Should I double underscore this?
        self.driver.get(self.URL) # Load the page
        delay = 6
        # Note: For xe.com the accept button is: <button class="button__BaseButton-sc-1qpsalo-0 haqezJ">
        # in the box <div class="fluid-container__BaseFluidContainer-qoidzu-0 gHjEXY ConsentBannerstyles__Banner-smyzu-1 dGQMCW">
        try:
            # Wait for the container to appear
            #WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@class="fluid-container__BaseFluidContainer-qoidzu-0 gHjEXY ConsentBannerstyles__Banner-smyzu-1 dGQMCW"]')))
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, container_path)))
            print("Cookies consent container found.")
            # Click on the accept button of the container
            #accept_button = self.driver.find_element(by = By.XPATH, '//*[@class="button__BaseButton-sc-1qpsalo-0 haqezJ"]')
            self.click_button(self, button_path)
            time.sleep(1)
        except TimeoutException:
            print("Time out: Failed to find the accept cookies button")
            print("Moving on...")
            # The rest of the script should work properly if the 'accept cookies' button is not found
    
    #def find_elements(self, container_path: str):
    # This can be written in the VNDBScraper


class VNDBScraper(Scraper):
    # Inherit Scraper. Consider putting this in a different py file
    pass
    


# Now scrape 

if __name__ == "__main__":
    scraper = Scraper('https://www.xe.com/', webdriver.Chrome(), '/raw_data')