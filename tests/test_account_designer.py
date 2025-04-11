from locators import Locators

class TestTransitions:

    def test_lk_to_designer(self, authorization):

        authorization.find_element(*Locators.BUTTON_LK).click()

    #переход по клику из личного кабинета на «Конструктор»
        authorization.find_element(*Locators.DESIGNER).click()

        actual_title = 'Соберите бургер'
        fact_title = authorization.find_element(*Locators.TITLE_ASSEMBLE_BURGER).text
        assert fact_title == actual_title

    def test_lk_to_main_logo(self, authorization):

    #переход в ЛК
        authorization.find_element(*Locators.BUTTON_LK).click()

    # переход по клику из личного кабинетана логотип Stellar Burgers.
        authorization.find_element(*Locators.MAIN_LOGO).click()

        actual_title = 'Соберите бургер'
        fact_title = authorization.find_element(*Locators.TITLE_ASSEMBLE_BURGER).text
        assert fact_title == actual_title


