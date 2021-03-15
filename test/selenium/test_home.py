"""
This module simulates user behavior via selenium and the default browser.
Test of home page.
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_homelink(self):
        """ test of all the links on the home page. """
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1382, 754)
        self.driver.find_element(By.LINK_TEXT, "About").click()
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        self.driver.find_element(By.LINK_TEXT,
                                 "contact@purbeurre.com").click()
        self.driver.find_element(By.LINK_TEXT, "contact").click()
        self.driver.find_element(By.LINK_TEXT, "mentions légales").click()
        self.driver.find_element(By.CSS_SELECTOR, ".navbar-brand").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
