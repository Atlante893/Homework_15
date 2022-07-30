from selenium.webdriver.common.by import By
from Homework_15.Framework_home_chrome.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    __email_input = (By.XPATH, "//input[@id='username']")
    __password_input = (By.ID, "password")
    __login_button = (By.XPATH, "//button[@type='submit']")
    user_dashboard = "https://app.memrise.com/dashboard"
    __greetings_message = (By.XPATH, "//h1")

    def __init__(self, driver):
        super().__init__(driver)

    def set_user_email(self, email):
        self.send_keys(self.__email_input, email)
        return self

    def set_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        self.wait_until_url_to_be(self.user_dashboard)

    def login(self, email, password):
        self.set_user_email(email)
        self.set_password(password)
        self.click_login_button()
        return self

    def get_greetings_message_text(self):
        text_element = self.wait_until_element_located(self.__greetings_message)
        return self.get_text(text_element)
