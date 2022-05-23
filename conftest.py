import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    print("\nstart browser..")
    browser = webdriver.Chrome()
    yield browser
    print("\nclose browser..")
    browser.quit()

