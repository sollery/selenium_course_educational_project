import time

from pages.cart_page import CartPage
from pages.main_page import MainPage
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options


def test_authorization():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service('C:\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=g,options=options)
    login = Login_page(driver)
    login.authorization()
    main_page = MainPage(driver)
    main_page.select_product()
    cart = CartPage(driver)
    cart.product_confirmation()
    time.sleep(10)

