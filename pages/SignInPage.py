from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    locator_dictionary = {
        "buttonGoToSignIn": (By.ID, 'nav-link-accountList'),
        "fieldEmail": (By.ID, 'ap_email'),
        "buttonContinue": (By.ID, 'continue')
        }

    @allure.step("Go to Sign In")
    def login(self):
        self.visit(self.base_url)
        self.find_element(*self.locator_dictionary['buttonGoToSignIn']).click()

    @allure.step("Send Username")
    def sendEmail(self):
        self.find_element(*self.locator_dictionary['fieldEmail']).send_keys('Spirlhark@gmail.com')

    @allure.step("Click Button Continue")
    def clickButtonContinue(self):
        self.find_element(*self.locator_dictionary['buttonContinue']).click()

    @allure.step('Examination')
    def examination(self):
        assert 1 == 2

