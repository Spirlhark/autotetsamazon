from tests_utils.session import Session
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class BasePage(object):

    def __init__(self, base_url=Session.BASE_URL):
        self.base_url = base_url
        self.browser = Session.get_driver()
        self.timeout = 30

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self, url):
        self.browser.get(url)

    def go_out(self):
        self.browser.quit()

    def button_esc(self):
        webdriver.ActionChains(self.browser).send_keys(Keys.ESCAPE).perform()

    def targeting(self, *loc):
        webdriver.ActionChains(self.browser).move_to_element(self.browser.find_element(*loc)).perform()
