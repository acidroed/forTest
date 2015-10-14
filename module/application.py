from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'acidroed'

class Application(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(base_url)
        self.wait = WebDriverWait(driver, 15)