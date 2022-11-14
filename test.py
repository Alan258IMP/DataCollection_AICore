# Alan Li, Imperial College London
# AICore 2022, all rights reserved

import unittest
from selenium.webdriver.common.by import By
from VNDBScraper import VNDBScraper
import time
import glob
from os import path

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        #scraper = VNDBScraper(headless=True)
        pass

    def test_load_and_reload(self):
        scraper = VNDBScraper(headless=True)
        default_page = 'https://vndb.org/v'
        time.sleep(0.2)
        self.assertEqual(scraper.driver.current_url, default_page)
        scraper.reload()
        self.assertEqual(scraper.driver.current_url, default_page)
    
    def test_next(self):
        scraper = VNDBScraper(headless=True)
        time.sleep(0.2)
        scraper.next()
        test = scraper.driver.current_url.startswith('https://vndb.org/v')
        self.assertTrue(test)
    
    def test_search(self):
        scraper = VNDBScraper(headless=True)
        time.sleep(0.2)
        scraper.search_keyword('yellow')
        test_search = scraper.driver.current_url.startswith('https://vndb.org/v?q=')
        self.assertTrue(test_search)
        # Search again to check if the previous entry is emptied
        scraper.search_keyword('grey')
        entry = scraper.driver.find_element(By.XPATH, '//*[@id="q"]').get_attribute('value')
        self.assertEqual(entry, 'grey')
    
    def test_get_info(self):
        scraper = VNDBScraper(headless=True)
        time.sleep(0.2)
        table_data = scraper.get_info()
        sample_dict = table_data[0]
        self.assertIsInstance(table_data, list)
        self.assertIsInstance(sample_dict, dict)
        self.assertIsInstance(sample_dict["Title"], str)
    
    def test_get_image(self):
        scraper = VNDBScraper(headless=True)
        time.sleep(0.2)
        image_url = scraper.download_img(URL = 'https://vndb.org/v729')
        test_url = image_url.startswith('https://s2.vndb.org/cv')
        # Get the file in the image folder just downloaded
        list_of_files = glob.glob('raw_data/images/*')
        image_path = max(list_of_files, key = path.getctime)
        ext = path.splitext(image_path)[1].lower()
        image_types = ['.jpg', '.jpeg', '.webp', '.png'] # These are the only types used at vndb.org
        is_image = (ext in image_types)
        self.assertIsInstance(image_url, str)
        self.assertTrue(test_url)

    
    def tearDown(self):
        #scraper.exit()
        pass

if __name__ == '__main__':
    unittest.main(exit=False)

