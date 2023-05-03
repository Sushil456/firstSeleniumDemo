import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options


class MicrosoftWA(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_MWA(self):
        
        options = Options()
        driver = webdriver.Firefox(options=options)
        wb = WebDriverWait(driver,4)
        driver.get("https://www.youtube.com/watch?v=9NmTZbbWqdI&ab_channel=AmeyaRecords")
        driver.maximize_window()
        wb.until(ec.presence_of_element_located((By.XPATH,'//button[@class="ytp-play-button ytp-button"]'))).click()
        wb.until(ec.presence_of_element_located((By.XPATH,'//button[@class="ytp-fullscreen-button ytp-button"]'))).click()
    
        time.sleep(435)
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
