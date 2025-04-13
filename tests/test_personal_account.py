from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestPersonalAccount:

    def test_lk_profile(self, authorization):

        authorization.find_element(*Locators.BUTTON_LK).click()

        WebDriverWait(authorization, 3).until(
            expected_conditions.visibility_of_element_located(Locators.TITLE_PROFILE))

        # переход по клику на «Личный кабинет». проверяем, что залогинились
        actual_header = 'Профиль'
        fact_header = authorization.find_element(*Locators.TITLE_PROFILE).text

        assert actual_header == fact_header

