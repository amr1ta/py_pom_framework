import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage
from tests.read_config import read_configfile

configFileName = 'configfile.ini'

class TestTemplate(unittest.TestCase):
    def setUp(self):
        browser = read_configfile(configFileName, 'userdata', 'browser')
        url = read_configfile(configFileName, 'userdata', 'url')
        if browser == 'chrome':
            self._driver = BasePage(webdriver.Chrome(ChromeDriverManager().install()))
        self._driver.open(url)

    def tearDown(self):
        self._driver.quit()
