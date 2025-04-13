from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import Parameters


class TestLogin:

    # вход по кнопке «Войти в аккаунт» на главной (описан в фикстуре)
    def test_login_main(self, authorization):

    #появилась кнопка "Оформить заказ"
        actual_header = 'Оформить заказ'
        fact_header = authorization.find_element(*Locators.BUTTON_PLACE_ORDER).text

        assert actual_header == fact_header

    # вход через кнопку «Личный кабинет»,
    def test_login_button_lk(self, driver_open):

        driver_open.find_element(*Locators.BUTTON_LK).click()

        # Ожидание появления заголовка
        WebDriverWait(driver_open, 3).until(
            expected_conditions.visibility_of_element_located(Locators.HEADER_ENTRANCE))

        driver_open.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(Parameters.EMAIL)
        driver_open.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(Parameters.PASSWORD)
        driver_open.find_element(*Locators.LOGIN_BUTTON_ENTRANCE).click()

        WebDriverWait(driver_open, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_ORDER))

    # появилась кнопка "Оформить заказ"
        actual_header = 'Оформить заказ'
        fact_header = driver_open.find_element(*Locators.BUTTON_PLACE_ORDER).text

        assert actual_header == fact_header


    # вход через кнопку в форме регистрации
    def test_login_form_registration(self, driver_open):

    #зайти на форму регистрации
        driver_open.find_element(*Locators.BUTTON_LK).click()
        driver_open.find_element(*Locators.LINK_REGISTRATION).click()
        driver_open.find_element(*Locators.LINK_LOGIN).click()

    #заполнить поля входа
        driver_open.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(Parameters.EMAIL)
        driver_open.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(Parameters.PASSWORD)
        driver_open.find_element(*Locators.LOGIN_BUTTON_ENTRANCE).click()

        WebDriverWait(driver_open, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_ORDER))

    # появилась кнопка "Оформить заказ"
        actual_header = 'Оформить заказ'
        fact_header = driver_open.find_element(*Locators.BUTTON_PLACE_ORDER).text

        assert actual_header == fact_header

   # вход через кнопку в форме восстановления пароля.
    def test_login_form_recover_password(self, driver_open):

    #зайти по кнопке Личный кабинет
        driver_open.find_element(*Locators.BUTTON_LK).click()

    #нажать Восстановить пароль
        driver_open.find_element(*Locators.LINK_RECOVER_PASSWORD).click()

    #нажать Войти
        driver_open.find_element(*Locators.LINK_LOGIN).click()

    #заполнить поля входа
        driver_open.find_element(*Locators.EMAIL_INPUT_XPATH).send_keys(Parameters.EMAIL)
        driver_open.find_element(*Locators.PASSWORD_INPUT_XPATH).send_keys(Parameters.PASSWORD)
        driver_open.find_element(*Locators.LOGIN_BUTTON_ENTRANCE).click()

        WebDriverWait(driver_open, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_ORDER))

    # появилась кнопка "Оформить заказ"
        actual_header = 'Оформить заказ'
        fact_header = driver_open.find_element(*Locators.BUTTON_PLACE_ORDER).text

        assert actual_header == fact_header
