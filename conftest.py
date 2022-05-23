import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser(cmdopt):
    print("\nstart browser..")
    link = f"http://selenium1py.pythonanywhere.com/{cmdopt}/catalogue/coders-at-work_207/"
    browser = webdriver.Chrome(link)
    yield browser
    print("\nclose browser..")
    browser.quit()



