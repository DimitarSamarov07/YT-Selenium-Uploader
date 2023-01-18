from time import sleep

import undetected_chromedriver as uc
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import xpathlist as xpath

runInVirtualDisplay = False


def initialize_driver():
    driver = uc.Chrome(version_main=108)
    driver.implicitly_wait(10)
    if runInVirtualDisplay:
        display = Display(visible=False, size=(800, 600))
        display.start()

    return driver


def signIn(driver: uc.Chrome, email, password):
    driver.get("https://www.youtube.com/")
    signInBtn = driver.find_element(By.XPATH, xpath.SIGN_IN_BUTTON)
    signInBtn.click()

    driver.find_element(By.XPATH, xpath.EMAIL_ADDRESS_INPUT).send_keys(email)
    driver.find_element(By.XPATH, xpath.NEXT_SIGN_IN).click()
    driver.find_element(By.XPATH, xpath.PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, xpath.NEXT_PASSWORD).click()
