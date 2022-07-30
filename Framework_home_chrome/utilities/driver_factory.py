from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    CHROME = 1
    FIRE_FOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id, is_headless):
        if DriverFactory.CHROME == driver_id:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        elif DriverFactory.FIRE_FOX == driver_id:
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        elif DriverFactory.EDGE == driver_id:
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        return driver
