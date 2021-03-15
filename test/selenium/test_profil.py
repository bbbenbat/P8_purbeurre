"""
This module simulates user behavior via selenium and the default browser.
Test of profil page.
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestProfil(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_profil(self):
        # Test name: profil
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(2576, 1066)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".nav-item:nth-child(4) img").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
