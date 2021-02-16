import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestFavorite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_favorite(self):
        # Test name: favorite
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 1456x607 |
        self.driver.set_window_size(1456, 607)
        # 3 | click | css=.nav-item:nth-child(4) img |
        self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) img").click()
        # 4 | click | id=id_login |
        self.driver.find_element(By.ID, "id_login").click()
        # 5 | type | id=id_login | testpurbeurre@gmail.com
        self.driver.find_element(By.ID, "id_login").send_keys("testpurbeurre@gmail.com")
        # 6 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 7 | type | id=id_password | AZERTY1234
        self.driver.find_element(By.ID, "id_password").send_keys("AZERTY1234")
        # 8 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 9 | click | css=.col-lg-8 .form-control |
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-8 .form-control").click()
        # 10 | type | css=.col-lg-8 .form-control | nutella
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-8 .form-control").send_keys("nutella")
        # 11 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 12 | click | xpath=(//button[@type='submit'])[2] |
        self.driver.find_element(By.XPATH, "(//button[@type=\'submit\'])[1]").click()
        time.sleep(1)
        # 13 | click | id=produrlbtn |
        self.driver.find_element(By.ID, "produrlbtn").click()
        # 3 | click | css=#myfavoritebtn img |
        self.driver.find_element(By.CSS_SELECTOR, "#myfavoritebtn img").click()
        # 4 | click | id=proddeletebtn |
        self.driver.find_element(By.ID, "proddeletebtn").click()


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
