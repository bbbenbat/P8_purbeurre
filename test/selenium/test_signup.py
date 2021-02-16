import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup(self):
        # Test name: signup
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 1382x754 |
        self.driver.set_window_size(1382, 754)
        # 3 | click | css=.nav-item:nth-child(5) img |
        self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) img").click()
        # 4 | click | id=id_first_name |
        self.driver.find_element(By.ID, "id_first_name").click()
        # 5 | type | id=id_first_name | test
        self.driver.find_element(By.ID, "id_first_name").send_keys("test")
        # 6 | type | id=id_last_name | retest
        self.driver.find_element(By.ID, "id_last_name").send_keys("retest")
        # 7 | type | id=id_email | retestbbessayah@gmail.com
        self.driver.find_element(By.ID, "id_email").send_keys("testpurbeurre@gmail.com")
        # 8 | click | id=id_password1 |
        self.driver.find_element(By.ID, "id_password1").click()
        # 9 | type | id=id_password1 | AZERTY1234
        self.driver.find_element(By.ID, "id_password1").send_keys("AZERTY1234")
        # 10 | type | id=id_password2 | AZERTY1234
        self.driver.find_element(By.ID, "id_password2").send_keys("AZERTY1234")
        # 11 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
