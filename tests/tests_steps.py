import pytest
from pages.SignInPage import SignInPage
from pages.Scenario2 import Scenario_Two
from pages.Scenario3 import Scenario_Three



@pytest.mark.usefixtures("start_session")
class TestLogin:
    def test_sign_in(self):
        sign_in = SignInPage()
        sign_in.login()
        sign_in.sendEmail()
        sign_in.clickButtonContinue()
        sign_in.examination()


@pytest.mark.usefixtures("start_session")
class TestScenario2:
    def test_scenario_2(self):
        test_scenario_2 = Scenario_Two()
        test_scenario_2.gotoTodaysDeals()
        test_scenario_2.clickOnCategory()
        test_scenario_2.clickElement()
        test_scenario_2.ordering()
        test_scenario_2.goToCart()
        test_scenario_2.price_comparison()
        test_scenario_2.number_of_units()
        test_scenario_2.check_total_price()


@pytest.mark.usefixtures("start_session")
class TestScenario3orders:
    def test_scenario_3_orders(self):
        test_scenario_3 = Scenario_Three()
        test_scenario_3.go_to_your_orders()


@pytest.mark.usefixtures("start_session")
class TestScenario3addresses:
    def test_scenario_3_addresses(self):
        test_scenario_3 = Scenario_Three()
        test_scenario_3.go_to_your_addresses()


@pytest.mark.usefixtures("start_session")
class TestScenario3lists:
    def test_scenario_3_lists(self):
        test_scenario_3 = Scenario_Three()
        test_scenario_3.go_to_your_lists()


