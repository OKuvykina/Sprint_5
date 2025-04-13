from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestLogout:

    def test_logout(self, authorization):

        authorization.find_element(*Locators.BUTTON_LK).click()
    # выход по кнопке «Выйти» в личном кабинете.
        WebDriverWait(authorization, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT))

        authorization.find_element(*Locators.LOGOUT).click()

        WebDriverWait(authorization, 3).until(
            expected_conditions.visibility_of_element_located(Locators.HEADER_ENTRANCE))

        actual_header = 'Вход'
        fact_header = authorization.find_element(*Locators.HEADER_ENTRANCE).text

        assert actual_header == fact_header
