"""
This module simulates user behavior via selenium and the default browser.
Test of favorite page.
"""

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFavorite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_favorite(self):
        # Test name: favorite
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1456, 607)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".nav-item:nth-child(4) img").click()
        self.driver.find_element(By.ID, "id_login").click()
        self.driver.find_element(By.ID, "id_login").send_keys(
            "testpurbeurre@gmail.com")
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("AZERTY1234")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".col-lg-8 .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".col-lg-8 .form-control").send_keys(
            "nutella")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.XPATH,
                                 "(//button[@type=\'submit\'])[1]").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "produrlbtn").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#myfavoritebtn img").click()
        self.driver.find_element(By.ID, "proddeletebtn").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
