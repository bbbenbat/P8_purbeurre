import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestResearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_produit(self):
        """ Test to find a product using the word 'coca'(step 4). """
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1382, 754)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".col-lg-8 .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".col-lg-8 .form-control").send_keys(
            "biscuit")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.XPATH,
                                 "//form[@id=\'produrl\']/button/p").click()
        self.driver.find_element(By.LINK_TEXT,
                                 "https://fr.openfoodfacts.org/"
                                 "produit/3175681134904/"
                                 "sable-nature-gerble").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
