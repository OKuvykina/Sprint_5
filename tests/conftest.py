import pytest
from selenium import webdriver
from data import Parameters
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture #заходим на страницу тестируемого сайта
def driver_open():

    driver = webdriver.Chrome()
    driver.set_window_size(1521, 703)
    driver.get(Parameters.URL)

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.TITLE_ASSEMBLE_BURGER))

    yield driver
    driver.quit()

@pytest.fixture #заполнение полей для входа и вход
def authorization(driver_open):

    driver_open.find_element(*Locators.LOGIN_BUTTON_IN_ACCOUNT).click()

    WebDriverWait(driver_open, 3).until(
        expected_conditions.visibility_of_element_located(Locators.HEADER_ENTRANCE))

    driver_open.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(Parameters.EMAIL)
    driver_open.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(Parameters.PASSWORD)
    driver_open.find_element(*Locators.LOGIN_BUTTON_ENTRANCE).click()

    WebDriverWait(driver_open, 3).until(
        expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_ORDER))

    return driver_open

