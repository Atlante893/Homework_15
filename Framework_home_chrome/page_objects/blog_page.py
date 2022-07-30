from selenium.webdriver.common.by import By

from Homework_15.Framework_home_chrome.page_objects.bienvenue_page import BienvenuePage
from Homework_15.Framework_home_chrome.utilities.web_ui.base_page import BasePage


class BlogPage(BasePage):
    about_us_page = "https://www.memrise.com/blog"
    __mem_news = (By.XPATH, "//h1/span")
    __image_travel = (By.XPATH, "//div/a/img[@style]")
    __start_learning_button = (By.XPATH, "//li/a[@href='https://app.memrise.com/bienvenue']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_mem_news_text(self):
        text_element = self.wait_until_element_located(self.__mem_news)
        return self.get_text(text_element)

    def get_image_travel(self):
        return self.is_element_visible(self.__image_travel)

    def click_start_learning_button(self):
        self.click(self.__start_learning_button)
        return BienvenuePage(self._driver)
