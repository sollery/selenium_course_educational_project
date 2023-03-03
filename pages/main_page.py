from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    select_product_1 = '//*[@id="add-to-cart-sauce-labs-backpack"]'
    cart = '//a[@class="shopping_cart_link"]'

    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions


    def click_select_product_1(self):
        self.get_select_product_1().click()
        print('Click select product 1')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart')

    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()