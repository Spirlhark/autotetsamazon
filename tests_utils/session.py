import time
from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from resorses.pars_values import getDataFromConfig

import os

os.environ['WDM_LOCAL'] = '1'
# os.environ['CI'] = 'True'


class Session:
    BASE_URL = getDataFromConfig('BASE_URL')
    LOCALE = 'en'

    @classmethod
    def set_settings(cls, browser):
        cls.browser = browser
        cls._driver = None

    @classmethod
    def start(cls):

        if cls._driver is None:
            cls._driver = cls.get_new_driver()
            cls._driver.get(cls.BASE_URL)
            cls.browser_version = cls._driver.capabilities[
                "browserVersion"] if 'browserVersion' in cls._driver.capabilities else '-'
            cls.platform = cls._driver.capabilities['platformName'] if 'platformName' in cls._driver.capabilities else '-'
            cls.browser_name = cls._driver.capabilities['browserName'] if 'browserName' in cls._driver.capabilities else '-'
        time.sleep(1)
        cls.main_window = cls._driver.current_window_handle

        return cls._driver


    @classmethod
    def get_new_driver(cls):
        if cls.browser == "chrome":
            options = cls._get_chrome_options()
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            # driver = vc.Chrome(use_subprocess=True, options=options)
            # driver = vc.Chrome(headless=True, options=options)
        elif cls.browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                            firefox_profile=cls._get_firefox_profile())
            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference("intl.accept_languages", Session.LOCALE)
            firefox_profile.update_preferences()
        elif cls.browser == "opera":
            options = cls._get_chrome_options()
            options.add_argument('allow-elevated-browser')
            if 'CI' not in os.environ:
                options.binary_location = r'/Applications/Opera.app/Contents/MacOS/Opera'
            else:
                options.binary_location = r'/usr/bin/opera'
            driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)
        elif cls.browser == "headless":
            options = cls._get_chrome_options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            # driver = vc.Chrome(use_subprocess=True)
            # driver = vc.Chrome(headless=True)
        elif cls.browser == "safari":
            driver = webdriver.Safari()
        else:
            assert False, f'Driver for end browser {cls.browser} not defined'
        # driver.set_window_size(1400, 1200)
        driver.maximize_window()
        driver.implicitly_wait(20)
        return driver

    @classmethod
    def get_driver(cls):
        return cls._driver

    @classmethod
    def get_browser_version(cls):
        try:
            return cls.browser_version
        except:
            return '-'

    @classmethod
    def get_platform(cls):
        try:
            return cls.platform
        except:
            return 'maza fucka'

    @classmethod
    def open(cls, url):
        pass
        # return cls._driver.get(url)

    @classmethod
    def quit(cls):
        cls._driver.quit()
        cls._driver = None

    @classmethod
    def switch_to_default_content(cls):
        cls._driver.switch_to.default_content()


    @classmethod
    def get_current_url(cls):
        return cls._driver.current_url

    @classmethod
    def switch_to_new_tab(cls):
        driver = cls.get_driver()
        driver.switch_to.window(driver.window_handles[-1])

    @classmethod
    def _get_chrome_options(cls):
        options = webdriver.ChromeOptions()
        options.add_argument(f"--lang={Session.LOCALE}")
        if 'CI' in os.environ:
            options.add_argument("--window-size=1400,1200")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-infobars")
        return options

    @classmethod
    def _get_firefox_capabilities(cls):
        capabilities = {}
        return capabilities

    @classmethod
    def get_session_id(cls):
        return cls.get_driver().session_id

    @classmethod
    def get_browser_name(cls):
        try:
            return cls.browser_name
        except:
            return '-'

    @classmethod
    def _get_firefox_profile(cls):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', Session.LOCALE)
        return profile


