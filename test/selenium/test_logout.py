import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestFavorite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_logout(self):
        # Test name: logout
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 2576x1066 |
        self.driver.set_window_size(2576, 1066)
        # 3 | click | css=#loginbtn img |
        self.driver.find_element(By.CSS_SELECTOR, "#loginbtn img").click()
        # 4 | click | id=id_login |
        self.driver.find_element(By.ID, "id_login").click()
        # 5 | click | id=id_login |
        self.driver.find_element(By.ID, "id_login").click()
        # 6 | type | id=id_login | testpurbeurre@gmail.com
        self.driver.find_element(By.ID, "id_login").send_keys("testpurbeurre@gmail.com")
        # 7 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 8 | type | id=id_password | AZERTY1234
        self.driver.find_element(By.ID, "id_password").send_keys("AZERTY1234")
        # 9 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 10 | click | css=#logoutbtn img |
        self.driver.find_element(By.CSS_SELECTOR, "#logoutbtn img").click()


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
