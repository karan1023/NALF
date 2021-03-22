from selenium.webdriver.common.by import By
from Locators.BasePage import BasePage
from Constants.config import TestData
import time


class LoginPageElements(BasePage):
    USERNAME = (By.ID, 'user_name')
    PASSWORD = (By.ID, 'password')
    CAPTCHA = (By.ID, 'captcha')
    LOGIN_BTN = (By.XPATH, '//button[text()="Login"]')
    LOGO = (By.CLASS_NAME, 'brand-logo')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASEURL)

    def do_login(self, username, password):
        self.do_click(self.USERNAME)
        self.do_send_keys(self.USERNAME, username)
        self.do_click(self.PASSWORD)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.CAPTCHA)
        time.sleep(6)
        self.do_click(self.LOGIN_BTN)
        time.sleep(3)

    def do_is_logo_visible(self):
        time.sleep(3)
        self.do_islogovisible(self.LOGO)
