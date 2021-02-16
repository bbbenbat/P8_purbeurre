import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestResearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_produit(self):
        """ Test to find a product using the word 'coca'(step 4),
        selection of a proposed product for the display of its description sheet (step 5),
        click on the link to be redirected to the page of this product on openfoodfact (step 6)."""
        # Test name: produit_coca
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 1382x754 |
        self.driver.set_window_size(1382, 754)
        # 3 | click | css=.col-lg-8 .form-control |
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-8 .form-control").click()
        # 4 | type | css=.col-lg-8 .form-control | coca
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-8 .form-control").send_keys("coca")
        # 5 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 6 | click | xpath=//form[@id='produrl']/button/p |
        self.driver.find_element(By.XPATH, "//form[@id=\'produrl\']/button/p").click()
        # 7 | click | linkText=https://fr.openfoodfacts.org/produit/5000112611762/coca-cola-zero-sucres-the-coca-cola-company |
        self.driver.find_element(By.LINK_TEXT,
                                 "https://fr.openfoodfacts.org/produit/5000112611762/coca-cola-zero-sucres-the-coca-cola-company").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
