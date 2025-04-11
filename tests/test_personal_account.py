from locators import Locators


class TestPersonalAccount:

    def test_lk_profile(self, authorization):

        authorization.find_element(*Locators.BUTTON_LK).click()

        # переход по клику на «Личный кабинет». проверяем, что залогинились
        actual_header = 'Профиль'
        fact_header = authorization.find_element(*Locators.TITLE_PROFILE).text

        assert actual_header == fact_header

