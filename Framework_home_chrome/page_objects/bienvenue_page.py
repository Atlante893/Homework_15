from selenium.webdriver.common.by import By

from Homework_15.Framework_home_chrome.page_objects.login_page import LoginPage
from Homework_15.Framework_home_chrome.utilities.web_ui.base_page import BasePage


class BienvenuePage(BasePage):
    bienvenue_page = "https://app.memrise.com/bienvenue"
    login_page = "https://app.memrise.com/signin"
    __login_button = (By.XPATH, "//a[@href='/signin']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_log_in(self):
        self.click(self.__login_button)
        self.wait_until_url_to_be(self.login_page)
        return LoginPage(self._driver)



