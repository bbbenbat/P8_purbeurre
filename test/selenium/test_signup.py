import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup(self):
        # Test name: signup
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1382, 754)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".nav-item:nth-child(5) img").click()
        self.driver.find_element(By.ID, "id_first_name").click()
        self.driver.find_element(By.ID, "id_first_name").send_keys("test")
        self.driver.find_element(By.ID, "id_last_name").send_keys("retest")
        self.driver.find_element(By.ID, "id_email").send_keys(
            "testpurbeurre@gmail.com")
        self.driver.find_element(By.ID, "id_password1").click()
        self.driver.find_element(By.ID, "id_password1").send_keys(
            "AZERTY1234")
        self.driver.find_element(By.ID, "id_password2").send_keys(
            "AZERTY1234")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
