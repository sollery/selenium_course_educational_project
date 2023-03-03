from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_class import Base


class ClientInfoPage(Base):
    url = 'https://www.saucedemo.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//*[@id="postal-code"]'
    continue_button = '//*[@id="continue"]'

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions

    def input_first_name(self, name):
        self.get_first_name().send_keys(name)
        print('input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('input lastname')

    def input_postal_code(self,code):
        self.get_postal_code().send_keys(code)
        print('Click login button')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue button')

    # Methods

    def input_information(self):
        self.get_current_url()
        self.input_first_name('test')
        self.input_last_name('test')
        self.input_postal_code('test')
        self.click_continue_button()