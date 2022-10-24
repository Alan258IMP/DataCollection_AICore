from WebScraper import Scraper
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
import pandas as pd

class VNDBScraper(Scraper):
    # Inherit Scraper. Consider putting this in a different py file
    def __init__(self, driver: webdriver.Chrome, URL: str = 'https://vndb.org/v', data_dir: str = 'raw_data', headless: bool = False):
        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--window-size=1600,900")
            chrome_options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=chrome_options)
        else:
            self.driver = driver
        self.URL = URL
        self.data_dir = data_dir
        if os.path.exists() == False:
            os.mkdir(data_dir)
        # Load page upon initialization (VNDB do not have cookies consent button)
        self.driver.get(self.URL)

    def search_keyword(self, keyword: str):
        '''
        Input a keyword into the search field and click the "search" button
        '''
        search_field = self.driver.find_element(By.XPATH, '//*[@id="q"]')
        search_field.clear()
        search_field.send_keys(keyword)
        search_button = self.driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/fieldset/input[2]')
        search_button.click()

    def next(self):
        '''
        Clicks the 'next' button on the page
        '''
        self.click_element(self, '/html/body/div[4]/form/div[2]/ul[2]/li[1]/a')
    
    def 
