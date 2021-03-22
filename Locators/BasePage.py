from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, data):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(data)

    def do_gettitle(self):
        return self.driver.title

    def do_islogovisible(self, by_locator):
        flag = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return flag
