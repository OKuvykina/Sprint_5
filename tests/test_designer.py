from locators import Locators


class TestDesigner:

    def test_designer_rolls(self, driver_open):
    # переход к разделу «Булки»
        driver_open.find_element(*Locators.SAUCES).click()
        driver_open.find_element(*Locators.ROLLS).click()

        actual_header = 'Булки'
        fact_header = driver_open.find_element(*Locators.ROLLS_CURRENT).text

        assert actual_header == fact_header

    def test_designer_sauces(self, driver_open):
    # переход к разделу «Соусы»
        driver_open.find_element(*Locators.SAUCES).click()

        actual_header = 'Соусы'
        fact_header = driver_open.find_element(*Locators.SAUCES_CURRENT).text

        assert actual_header == fact_header

    def test_designer_toppings(self, driver_open):
    # переход к разделу «Начинки»
        driver_open.find_element(*Locators.TOPPINGS).click()

        actual_header = 'Начинки'
        fact_header = driver_open.find_element(*Locators.TOPPINGS_CURRENT).text

        assert actual_header == fact_header
