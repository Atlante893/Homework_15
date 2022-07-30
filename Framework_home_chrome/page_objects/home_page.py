from selenium.webdriver.common.by import By

from Homework_15.Framework_home_chrome.page_objects.bienvenue_page import BienvenuePage
from Homework_15.Framework_home_chrome.page_objects.blog_page import BlogPage
from Homework_15.Framework_home_chrome.page_objects.login_page import LoginPage
from Homework_15.Framework_home_chrome.utilities.web_ui.base_page import BasePage


class HomePage(BasePage):
    __login_button = (By.XPATH, "//div [@class='mem-rise-top-header-menu']/ul/li/a")
    __logo_memrise = (By.XPATH, "//img[@alt='memrise logo']")
    __learn_to_speak = (By.XPATH, "//h1")
    __start_learning_button = (By.XPATH, "//li/a[@href='https://app.memrise.com/bienvenue']")
    __blog_button = (By.XPATH, "//a[@href='https://www.memrise.com/blog']")
    __image_background = (By.XPATH, "//div[contains(@class,'v3-girl-hero-image-tablet')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_log_in(self):
        self.click(self.__login_button)
        return LoginPage(self._driver)

    def get_logo_memrise(self):
        return self.is_element_visible(self.__logo_memrise)

    def get_learn_to_speak_text(self):
        text_element = self.wait_until_element_located(self.__learn_to_speak)
        return self.get_text(text_element)

    def click_start_learning_button(self):
        self.click(self.__start_learning_button)
        return BienvenuePage(self._driver)

    def click_blog_button(self):
        self.click(self.__blog_button)
        return BlogPage(self._driver)

    def get_image_background(self):
        return self.is_element_visible(self.__image_background)
