from selenium.webdriver.common.by import By

class Locators:

    LOGIN_BUTTON_IN_ACCOUNT = (By.XPATH, "//*[contains(@class, 'button_button_size_large') and text()='Войти в аккаунт']") #кнопка Войти в аккаунт
    LOGIN_BUTTON_ENTRANCE = (By.XPATH, "//*[contains(@class, 'button_button_size_medium') and text()='Войти']") #кнопка Войти на форме входа

    BUTTON_LK = (By.XPATH, "//*[contains(@class, 'AppHeader_header__linkText') and text()='Личный Кабинет']") #кнопка Личный Кабинет
    NAME_INPUT_XPATH = [By.XPATH,
                        "//label[text()='Имя']/following-sibling::input[@name='name']"]  # Окно регистрации, поле 'Имя'
    EMAIL_INPUT_XPATH = [By.XPATH,
                            "//label[text()='Email']/following-sibling::input[@name='name']"]  # Окно регистрации, поле 'Email'

    PASSWORD_INPUT_XPATH = [By.XPATH,
                            "//label[text()='Пароль']/following-sibling::input[@name='Пароль']"]  # Окно регистрации, поле 'Пароль'
    HEADER_ENTRANCE = (By.XPATH, "//h2[text()='Вход']") #Заголовок Вход
    INCORRECT_PASSWORD = (By.XPATH, "//p[contains(@class, 'text_type_main-default') and text()='Некорректный пароль']")
    BUTTON_REGISTRATION = (By.XPATH, "//*[contains(@class,'button_button_size_medium') and text()='Зарегистрироваться']")
    LINK_REGISTRATION = (By.XPATH, "//a[text()='Зарегистрироваться']")
    LINK_RECOVER_PASSWORD = (By.XPATH,"//a[text()='Восстановить пароль']")
    LINK_LOGIN = (By.XPATH,"//a[text()='Войти']")
    BUTTON_PLACE_ORDER = (By.XPATH, "//*[contains(@class,'button_button_size_large') and text()='Оформить заказ']") #кнопка "Оформить заказ"
    TITLE_PROFILE = (By.XPATH, "//*[contains(@class,'Account_link_active') and text()='Профиль']") #заголовок "Профиль" в Личном кабинете
    DESIGNER = (By.XPATH,"//p[text()='Конструктор']")
    TITLE_ASSEMBLE_BURGER = (By.XPATH,"//h1[text()='Соберите бургер']")
    MAIN_LOGO = (By.XPATH,"//*[contains(@class,'AppHeader_header__logo')] ")
    LOGOUT = (By.XPATH, "//*[contains(@class,'text_color_inactive') and text()='Выход']")
    ROLLS = (By.XPATH, "//*[contains(@class,'text_type_main-default') and text()='Булки']")
    SAUCES = (By.XPATH, "//*[contains(@class,'text_type_main-default') and text()='Соусы']")
    TOPPINGS = (By.XPATH, "//*[contains(@class,'text_type_main-default') and text()='Начинки']")

    ROLLS_CURRENT = (By.XPATH, "//*[contains(@class,'tab_type_current')]/*[text()='Булки']")
    SAUCES_CURRENT= (By.XPATH, "//*[contains(@class,'tab_type_current')]/*[text()='Соусы']")
    TOPPINGS_CURRENT = (By.XPATH, "//*[contains(@class,'tab_type_current')]/*[text()='Начинки']")