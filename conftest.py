import pytest
from selenium import webdriver
import  time


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="None", help="Chooice some language"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("--language")
    browser = None
    print(browser_lang)
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    link = "http://selenium1py.pythonanywhere.com/" + str(browser_lang) + "/catalogue/coders-at-work_207/"
    print(link)
    print("\nstart chrome browser for test..")
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()