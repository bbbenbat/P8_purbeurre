import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_homelink(self):
        """ test of all the links on the home page.
        Link in menu, 'about' section (step 3).
        Link in menu, 'Contact' section (step 4).
        Email redirection (step 5).
        Page footer, 'Contact' redirection (step 6).
        Footer, redirection 'Legal notice' (step 7). """
        # Test name: home_link
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 1382x754 |
        self.driver.set_window_size(1382, 754)
        # 3 | click | linkText=About |
        self.driver.find_element(By.LINK_TEXT, "About").click()
        # 4 | click | linkText=Contact |
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        # 5 | click | linkText=contact@purbeurre.com |
        self.driver.find_element(By.LINK_TEXT, "contact@purbeurre.com").click()
        # 6 | click | linkText=contact |
        self.driver.find_element(By.LINK_TEXT, "contact").click()
        # 7 | click | linkText=mentions légales |
        self.driver.find_element(By.LINK_TEXT, "mentions légales").click()
        # 8 | click | css=.navbar-brand |
        self.driver.find_element(By.CSS_SELECTOR, ".navbar-brand").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
