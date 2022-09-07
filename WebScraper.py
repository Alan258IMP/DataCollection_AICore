# Alan Li, Imperial College London
# AICore 2022, all rights reserved

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import urllib
import requests
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
    parent_dir: str
    The parent directory in which the data will be stored.

    Attributes:
    ----------

    Methods:
    -------
    '''

    def __init__(self, URL: str, driver: webdriver.Chrome, parent_dir: str):
        self.driver = driver
        self.URL = URL


    def _load_and_accept_cookies(self):
        #Should I double underscore this?
        self.driver.get(self.URL)
        accept_button = self.driver.find_element(by=By.XPATH, value="//*[@class='btn btn-success acceptGdpr']") #?
        accept_button.click()
    
    # TODO: scrolling, clicking on links, send keystrokes
    def 



# Now scrape 