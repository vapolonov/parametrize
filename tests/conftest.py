# import pytest
# from selene.support.shared import browser
# from selenium import webdriver
#
#
# @pytest.fixture(params=[(1920, 1080), (1024, 960)])
# def browser_config(request):
#     chrome_options = webdriver.ChromeOptions()
#     browser.config.base_url = 'https://demoqa.com'
#     browser.config.chrome_options = chrome_options
#     browser.config.window_width = request.param[0]
#     browser.config.window_height = request.param[1]
#     yield browser
#     browser.quit()
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=[
    {'browser_name': 'chrome', 'window_size': (1920, 1080)},
    {'browser_name': 'chrome', 'window_size': (1366, 768)},
    {'browser_name': 'firefox', 'window_size': (1920, 1080)},
    {'browser_name': 'firefox', 'window_size': (1366, 768)}
])
def browser_config(request):
    if request.param['browser_name'] == 'chrome':
        chrome_options = ChromeOptions()
        browser.config.driver = webdriver.Chrome(options=chrome_options)
    elif request.param['browser_name'] == 'firefox':
        firefox_options = FirefoxOptions()
        browser.config.driver = webdriver.Firefox(options=firefox_options)

    browser.config.base_url = 'https://demoqa.com'

    browser.config.window_width = request.param['window_size'][0]
    browser.config.window_height = request.param['window_size'][1]

    yield browser

    browser.quit()

