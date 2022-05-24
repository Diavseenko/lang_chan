import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="None", help="Chooice some language"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("--language")
    browser = None
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    link1 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    link2 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    if browser_lang == "en":
        print("\nstart chrome browser for test..")
        browser.get(link1)

    elif browser_lang == "ru":
        print("\nstart chrome browser for test..")
        browser.get(link2)

    else:
        raise pytest.UsageError("check your language")
    yield browser
    print("\nquit browser..")
    browser.quit()


#@pytest.fixture()
#def browser(request):
#    print("\nstart browser..")
#    browser = webdriver.Chrome()
#    yield browser
#    print("\nclose browser..")
#    browser.quit()