from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By


class Scenario_Three(BasePage):
    locator_dictionary = {
        "buttonGoToSignIn": (By.ID, 'nav-link-accountList'),
        "buttonYourOrders": (By.XPATH, '//*[@id="nav_prefetch_yourorders"]/span'),
        "buttonYourAddresses": (By.XPATH, '//*[@id="nav_prefetch_youraddresses"]/span'),
        "buttonYourLists": (By.XPATH, '//*[@id="nav-al-your-account"]/a[4]/span')
        }

    @allure.step("Go to Your Orders")
    def go_to_your_orders(self):
        self.visit(self.base_url)
        self.targeting(*self.locator_dictionary['buttonGoToSignIn'])
        self.find_element(*self.locator_dictionary['buttonYourOrders']).click()
        assert 1 == 2

    @allure.step("Go to Your Addresses")
    def go_to_your_addresses(self):
        self.visit(self.base_url)
        self.targeting(*self.locator_dictionary['buttonGoToSignIn'])
        self.find_element(*self.locator_dictionary['buttonYourAddresses']).click()
        assert 1 == 2

    @allure.step("Go to Your Lists")
    def go_to_your_lists(self):
        self.visit(self.base_url)
        self.targeting(*self.locator_dictionary['buttonGoToSignIn'])
        self.find_element(*self.locator_dictionary['buttonYourLists']).click()
        assert self.browser.current_url == 'https://www.amazon.ae/hz/wishlist/intro'

