# Alan Li, Imperial College London
# AICore 2022, all rights reserved

from email.policy import default
import unittest
import os
from WebScraper import Scraper
from VNDBScraper import VNDBScraper
import time

class ScraperTestCase(unittest.TestCase):
    def test_load_and_reload(self):
        scraper = VNDBScraper(headless=True)
        default_page = 'https://vndb.org/v'
        time.sleep(0.5)
        test_load = (scraper.driver.current_url == default_page)
        scraper.reload()
        test_reload = (scraper.driver.current_url == default_page)
        scraper.exit()
        self.assertTrue(test_load)
        self.assertTrue(test_reload)
    
    def test_next(self):
        scraper = VNDBScraper(headless=True)
        time.sleep(0.5)
        scraper.next()
        test = (scraper.driver.current_url == 'https://vndb.org/v?f=&p=2')
        scraper.exit()
        self.assertTrue(test)
    
    def test_search(self):
        scraper = VNDBScraper(headless=True)
        time.sleep(0.5)
        scraper.search_keyword('yellow')
        test_search1 = scraper.driver.current_url.startswith('https://vndb.org/v?q=')
        # Search again to check if the previous entry is emptied
        scraper.search_keyword('grey')
        entry = scraper.driver.find_element(By.XPATH, '//*[@id="q"]').get_attribute('value')
        test_search2 = (entry == 'grey')
        scraper.exit()
        self.assertTrue(test_search1)
        self.assertTrue(test_search2)
    # Write the rest of the tests after finalizing VNDB
        
        
        




if __name__ == '__main__':
    unittest.main(exit=False)

