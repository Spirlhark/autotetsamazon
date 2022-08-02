import collections
import json
import os

import allure
import pytest


from tests_utils.session import Session


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in browser name headless, chrome, firefox, opera")


# @pytest.hookimpl(trylast=True)
def pytest_configure(config):
    browser = config.getoption("--browser")
    Session.set_settings(browser)
    # allure.environment(test_server='testserver')
    # allure.environment(test_server='testserver', report='My Test Report')


def pytest_sessionstart(session):
    session.results = dict()
    # session.config.allure.environment(test_server='testserver', report='My Test Report')


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if Session.get_driver() is not None and (report.when == 'call'):
        item.session.results[item] = report
        allure.attach(
            Session.BASE_URL,
            name='Current URL',
            attachment_type=allure.attachment_type.URI_LIST
        )
    if Session.get_driver() is not None and (report.when == 'call' or report.when == 'setup'):
        item.session.results[item] = report
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            allure.attach(
                Session.get_driver().get_screenshot_as_png(),
                name='Screenshot',
                attachment_type=allure.attachment_type.PNG
            )


def pytest_sessionfinish(session):
    # Add environment in allure report
    report_dir = session.config.option.allure_report_dir  # Gets the --alluredir directory path
    if report_dir:
        env_details = collections.OrderedDict(Dimka='KraSav4ik',
                                              Browser=Session.get_browser_name(),
                                              Version=Session.get_browser_version(),
                                              isHeadless='True',
                                              BASE_URL='https://www.google.com/account/'
                                              )
        with open('{}/{}'.format(report_dir, 'environment.properties'), 'w') as _f:
            data = '\n'.join([f'{variable}={value}' for variable, value in env_details.items()])
            _f.write(data)
    ## Add executor in allure report
    #     if 'CI' in os.environ:
    #         executor = dict(name='Bitbucket',
    #                         type="CI",
    #                         buildUrl=os.environ['BITBUCKET_GIT_HTTP_ORIGIN']+'/addon/pipelines/home#!/results/'+os.environ['BITBUCKET_BUILD_NUMBER'],
    #                         buildName=os.environ['BITBUCKET_BRANCH'])
    #         with open('{}/{}'.format(report_dir, 'executor.json'), 'w') as _f:
    #             json.dump(executor, _f)


@pytest.fixture(scope="class")
def start_session():
    Session.start()
    yield
    Session.quit()


# @pytest.fixture(scope="class")
# def log_in():
#     LoginSteps.ui_login_main_user()
#     BaseSteps.close_all_modals()

# @pytest.fixture(scope="class")
# def log_in_api():
#     AuthSteps.login(Config().get_username(), Config().get_password(), Config().get_url('main'))
#     Session.open(Config().get_url('main'))
#     # BaseSteps.close_all_modals()


@pytest.fixture(scope="function")
def open_url(request):
    Session.open(request.cls.url)


@pytest.fixture(scope="function")
def open_url_without_log_in(request):
    Session.open(request.cls.url)


@pytest.fixture(scope="function")
def open_test_url(request):
    url = request.node.get_closest_marker('open_url').args[0]
    Session.open(url)


# @pytest.fixture(scope="function")
# def start_session_func_with_log_in():
#     Session.start()
#     LoginSteps.ui_login_main_user()
#     yield
#     Session.quit()


@pytest.fixture(scope="function")
def start_session_func_without_log_in():
    Session.start()
    yield
    Session.quit()
