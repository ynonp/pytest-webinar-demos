from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='session', params=[webdriver.Chrome])
def browser(request):
    options = Options()
    options.headless = True
    driver = request.param(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.close()


