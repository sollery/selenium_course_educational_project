from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_class import Base


class PaymentPage(Base):
    url = 'https://www.saucedemo.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    finish_button = '//button[@id="finish"]'

    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    # Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print('Click finish button')

    # Methods

    def payment(self):
        self.get_current_url()
        self.click_finish_button()
