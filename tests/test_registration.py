import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from DATA import Parameters

class Test_Registration:

#успешная регистрация
    def test_registration_success(self, driver_open, generation_email):

    #через кнопку Личный кабинет заходим на форму регистрации
        driver_open.find_element(*Locators.BUTTON_LK).click()
        driver_open.find_element(*Locators.LINK_REGISTRATION).click()

    #заполняем форму регистрации
        driver_open.find_element(*Locators.NAME_INPUT_XPATH).send_keys(Parameters.NAME)
        driver_open.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(generation_email)
        driver_open.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(Parameters.PASSWORD)
        driver_open.find_element(*Locators.BUTTON_REGISTRATION).click()

    # Ожидание появления заголовка
        WebDriverWait(driver_open, 3).until(
            expected_conditions.visibility_of_element_located(Locators.HEADER_ENTRANCE))

    #проверка на заголовок "Вход" - значит, что регистрация успешна
        actual_header = 'Вход'
        fact_header = driver_open.find_element(*Locators.HEADER_ENTRANCE).text
        assert fact_header == actual_header

    #некорректный пароль
    @pytest.mark.parametrize('incorrect_password', ['1', '1abcd', '123$#', '     ', '123 4'])
    def test_registration_fail_incorrect_password(self, driver_open, incorrect_password, generation_email):

        driver_open.find_element(*Locators.BUTTON_LK).click()
        driver_open.find_element(*Locators.LINK_REGISTRATION).click()

        driver_open.find_element(*Locators.NAME_INPUT_XPATH).send_keys('OLGA')
        driver_open.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(generation_email)
        driver_open.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(incorrect_password)

        driver_open.find_element(*Locators.BUTTON_REGISTRATION).click()

    #проверка на заголовок "Некорректный пароль"
        actual_title = 'Некорректный пароль'
        fact_title = driver_open.find_element(*Locators.INCORRECT_PASSWORD ).text
        assert fact_title == actual_title
