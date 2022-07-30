import pytest
from contextlib import suppress
from datetime import datetime
from Homework_15.Framework_home_chrome.page_objects.home_page import HomePage
from Homework_15.Framework_home_chrome.utilities.driver_factory import DriverFactory
from Homework_15.Framework_home_chrome.utilities.read_run_settings import ReadConfig


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def create_driver_chrome(request):
    driver = DriverFactory.create_driver(driver_id=int(ReadConfig.get_driver_id()),
                                         is_headless=False)
    driver.maximize_window()
    driver.get(ReadConfig.get_application_url())
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            test_name = request.node.name + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            take_screenshot(driver, test_name)
    driver.quit()


def take_screenshot(create_driver_chrome, test_name):
    screenshots_dir = "../screenshots"
    screenshot_file_name = "{}/{}.png".format(screenshots_dir, test_name)
    create_driver_chrome.save_screenshot(screenshot_file_name)


@pytest.fixture
def get_home_page(create_driver_chrome):
    return HomePage(create_driver_chrome)
