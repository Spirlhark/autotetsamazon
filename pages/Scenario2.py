import time
from resorses.pars_values import getDataFromConfig
import nums_from_string
from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Scenario_Two(BasePage):
    locator_dictionary = {
        "buttonGoToTodaysDeals": (By.XPATH, '//*[@id="nav-xshop"]/a[3]'),
        # "2category": (By.XPATH, '//*[@id="slot-15"]/div/div/div[2]/div[3]/div/div[2]'),
        "2category": (By.XPATH, '//*[@id="slot-15"]/div/div/div[2]/div[3]/div/div[1]'),
        "buttonElements": (By.XPATH, '//*[@id="octopus-dlp-asin-stream"]/ul/li[1]'),
        "priceWhenOrdering": (By.XPATH, '//*[@id="corePrice_feature_div"]/div/span/span[2]'),
        "clickQuantity": (By.ID, 'quantity'),
        "addToCartButton": (By.ID, 'add-to-cart-button'),
        "cartButton": (By.ID, 'nav-cart'),
        "unitsInTheCart": (By.XPATH, '//*[@id="sc-subtotal-label-activecart"]'),
        "priceInTheCart": (By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[3]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[2]/p/span'),
        "totalPriceInCart": (By.XPATH, '//*[@id="sc-subtotal-amount-activecart"]/span')
        }

    price_when_ordering = 0
    price_in_the_cart = 1
    units_in_the_cart = 2
    total_price_in_cart = 4

    @allure.step("Go to Today's Deals")
    def gotoTodaysDeals(self):
        self.visit(self.base_url)
        self.find_element(*self.locator_dictionary['buttonGoToTodaysDeals']).click()

    @allure.step("Click on 2nd category")
    def clickOnCategory(self):
        self.find_element(*self.locator_dictionary['2category']).click()

    @allure.step("Click Element")
    def clickElement(self):
        self.find_element(*self.locator_dictionary['buttonElements']).click()

    @allure.step("Ordering")
    def ordering(self):
        # price = self.find_element(*self.locator_dictionary['priceWhenOrdering']).text
        # qwe = nums_from_string.get_nums(price)
        # price01 = qwe[0]
        Scenario_Two.price_when_ordering = nums_from_string.get_nums(self.find_element(*self.locator_dictionary['priceWhenOrdering']).text)[0]
        Select(self.find_element(*self.locator_dictionary['clickQuantity'])).select_by_value(f'{getDataFromConfig("UNIT")}')
        self.find_element(*self.locator_dictionary['addToCartButton']).click()
        self.button_esc()

    @allure.step("Go To Cart")
    def goToCart(self):
        self.find_element(*self.locator_dictionary['cartButton']).click()
        Scenario_Two.units_in_the_cart = nums_from_string.get_nums(self.find_element(*self.locator_dictionary['unitsInTheCart']).text)[0]
        Scenario_Two.price_in_the_cart = nums_from_string.get_nums(self.find_element(*self.locator_dictionary['priceInTheCart']).text)[0]
        Scenario_Two.total_price_in_cart = nums_from_string.get_nums(self.find_element(*self.locator_dictionary['totalPriceInCart']).text)[0]

    @allure.step('Price Comparison')
    def price_comparison(self):
        assert Scenario_Two.price_when_ordering == Scenario_Two.price_in_the_cart

    @allure.step('Check the Number of Units Ordered')
    def number_of_units(self):
        assert Scenario_Two.units_in_the_cart == getDataFromConfig('UNIT')

    @allure.step('Check Total Price')
    def check_total_price(self):
        assert Scenario_Two.total_price_in_cart == Scenario_Two.price_in_the_cart * getDataFromConfig('UNIT')
