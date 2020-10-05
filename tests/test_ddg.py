# coding=utf8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_title():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.get('https://duckduckgo.com')
    assert browser.title == u'DuckDuckGo \u2014 Privacy, simplified.'
    browser.close()


def test_logo(browser):
    browser.get('https://duckduckgo.com')
    a = browser.find_element_by_css_selector('a#logo_homepage_link')
    assert a.get_attribute('href') == "https://duckduckgo.com/about"
