from WebScraper import Scraper
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
    def __init__(self, driver: webdriver.Chrome = webdriver.Chrome(), URL: str = 'https://vndb.org/v', data_dir: str = 'raw_data', headless: bool = False):
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
        Input a keyword into the search field, then click the "search" button
        '''
        search_field = self.driver.find_element(By.XPATH, '//*[@id="q"]')
        search_field.clear()
        search_field.send_keys(keyword)
        search_button = self.driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/fieldset/input[2]')
        time.sleep(0.5)
        search_button.click()
        time.sleep(1)

    def next(self):
        '''
        Go to the next page (works for novel list page only)
        If the button is not found (meaning you're on the last page), the code proceeds.
        '''
        self.click_element(self, '/html/body/div[4]/form/div[2]/ul[2]/li[1]/a')
    
    def get_info(self, filename = 'data.json', limit = 50):
        '''
        Get the information of all the search results on the page
        '''
        table = self.driver.find_element(By.XPATH, '/html/body/div[4]/form/div[3]/table/tbody')
        rows = table.find_elements(By.XPATH, './tr')
        table_data = [] # going to be a list of dictionaries

        for row in rows[:5]:
            row_elements = row.find_elements(By.XPATH, './td')
            title = row_elements[0].text
            release_date = row_elements[3].text
            popularity = row_elements[4].text
            rating = row_elements[5].text.split()[0]
            no_of_voters = int(row_elements[5].text.split()[1][1:-1]) # need to take away brackets

            # Platforms and languages are displayed in images, need to be dealt with separately
            platforms = []
            languages = []
            platforms_img = row_elements[1].find_elements(By.XPATH, './img')
            languages_img = row_elements[2].find_elements(By.XPATH, './abbr')
            for platform in platforms_img:
                platforms.append(platform.get_attribute('title'))
            platforms = ", ".join(platforms)
            for language in languages_img:
                languages.append(language.get_attribute('title'))
            languages = ", ".join(languages)
            # Get description page link
            description_page_url = row_elements[0].find_element(By.XPATH, './a').get_attribute('href')

            row_data_dict = {"URL": description_page_url,
                            "Title": title,
                            "Platform_available": platforms,
                            "Language_available": languages,
                            "Release_date": release_date,
                            "Popularity": popularity,
                            "Rating": rating,
                            "No_of_voters": no_of_voters}
            table_data.append(row_data_dict)



        dataframe = pd.DataFrame(table_data)
        dataframe.to_json('data.json')


if __name__ == "__main__":
    scraper = VNDBScraper(headless=False)
    keyword = input()
    scraper.search_keyword(keyword)

    Scraper('https://www.xe.com/', webdriver.Chrome(), '/raw_data')
