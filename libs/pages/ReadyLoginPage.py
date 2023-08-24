""" ReadyLoginPage.py """
#pylint: disable=W0401
#pylint: disable=W0614
#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0707
#pylint: disable=W0702

import inspect
from CommonLibrary import CommonLibrary
from selenium.webdriver.common.by import By


class ReadyLoginPage(CommonLibrary):
    """ Class: ReadyLoginPage """
    login_frame = 'login-iframe'
    username_txt = '#username'
    password_txt = '#password'
    login_button = '#kc-login'
    remember_me_checkbox = '#rememberMe'
    forget_password_link = '#kc-forgot-pword-link'
    logout_button = 'div[data-test-id="ProductDashboardMenu-DashboardMenu-DashboardMenuOption-logout"], div:nth-child(2) > a > div'
    invalid_credentials = 'div[class="alert alert-error"] span[class="c-snackbar--error"]'
    reset_password_header = 'h2[class="kc-page-title"]'
    terms_and_cond = '//*[contains(text(),"Terms and conditions")]'
    terms_and_cond_checkbox = '#acceptTerms'
    terms_and_cond_accept_btn = '#kc-accept-button'
    login_access_denied = 'pre:nth-child(1)'

    def log_in(self, username, password, checkLogoutBtn=True):
        """ Method: log_in """
        try:
            username = str(self.data[username])
            password = str(self.data[password])

            browsername = self.driver.capabilities['browserName']
            browserversion = self.driver.capabilities['browserVersion']
            print(f"Browser: {browsername}")
            print(f"Version: {browserversion}")
            print("Logging into Ready as: {}".format(username))
            self.driver.switch_to.frame(ReadyLoginPage.login_frame)
            self.clear_field(ReadyLoginPage.username_txt)
            self.enter_text(ReadyLoginPage.username_txt, username)
            self.enter_text(ReadyLoginPage.password_txt, password)
            self.click_element(ReadyLoginPage.remember_me_checkbox)
            self.click_element(ReadyLoginPage.login_button)
            try:
                terms_and_condition = self.driver.find_element_by_xpath(ReadyLoginPage.terms_and_cond)
            except:
                terms_and_condition = []
            if terms_and_condition != []:
                self.generate_screenshot("TOS_change_identified.")
                self.click_element(ReadyLoginPage.terms_and_cond_checkbox)
                self.click_element(ReadyLoginPage.terms_and_cond_accept_btn)
            handles = self.driver.window_handles
            size = len(handles)
            for num in range(size):
                self.driver.switch_to.window(handles[num])
            if checkLogoutBtn:
                self.element_present(ReadyLoginPage.logout_button)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to log into Ready due to:" + str(error))

    def login_negative(self, username, password):
        """ login_negative """
        try:
            print("Logging into Ready as: {}".format(username))
            self.driver.switch_to.frame(ReadyLoginPage.login_frame)
            if username != "blank":
                self.enter_text(ReadyLoginPage.username_txt, username)
            if password != "blank":
                self.enter_text(ReadyLoginPage.password_txt, password)

            self.click_element(ReadyLoginPage.remember_me_checkbox)
            self.click_element(ReadyLoginPage.login_button)
            error_message = self.get_text(ReadyLoginPage.invalid_credentials)
            print("Got error: {}".format(error_message))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to login negative Ready test due to:" + str(error))

    def login_with_no_permission(self, username, password):
        """ Method: login_with_no_permission """
        try:
            username = str(self.data[username])
            password = str(self.data[password])

            print("Logging into Ready as: {}".format(username))
            self.driver.switch_to.frame(ReadyLoginPage.login_frame)
            self.clear_field(ReadyLoginPage.username_txt)
            self.enter_text(ReadyLoginPage.username_txt, username)
            self.enter_text(ReadyLoginPage.password_txt, password)
            self.click_element(ReadyLoginPage.remember_me_checkbox)
            self.click_element(ReadyLoginPage.login_button)

            access_denied_error = self.driver.find_element(By.CSS_SELECTOR, ReadyLoginPage.login_access_denied).text
            print("Got login access denied error: {}".format(access_denied_error))
            assert access_denied_error.__contains__("unable to verify the ID token required scope"), \
                "Wrong access deny error!"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to get login access denied permission error due to: {}".format(error))

    def log_out(self):
        """ Method: log_out """
        try:
            self.click_element(ReadyLoginPage.logout_button)
            print("Logged out from Ready")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to log out from Ready due to:" + str(error))

    def click_forgot_password(self):
        """ Method: click_forgot_password """
        try:
            self.driver.switch_to.frame(ReadyLoginPage.login_frame)
            self.click_element(ReadyLoginPage.forget_password_link)
            actual_header = self.get_text(ReadyLoginPage.reset_password_header)
            print("Got header: {}".format(actual_header))
            assert actual_header == "Reset password", "Expected: 'Reset password'"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to click 'Forgot password' link due to: " + str(error))

    def navigate_to_url(self, url):
        """ Method: navigate_to_url """
        try:
            print(f"Navigating to URL: {url}...")
            if "staging" in url:
                print("Setting to EN locale!")
                locale = "https://auth.staging.onec.co/auth/realms/oneconcern/login-actions/authenticate?kc_locale=en"
                self.driver.get(locale)
            self.driver.get(url)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception(f"Fail to navigate to the URL: {url} due to: " + str(error))
