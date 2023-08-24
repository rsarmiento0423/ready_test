""" ReadyLibraryPage.py """
#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0707
#pylint: disable=W0401
#pylint: disable=R0904
#pylint: disable=W0614
#pylint: disable=W0201
import inspect
import time
from selenium.webdriver.common.keys import Keys
from ReadyLivePage import ReadyLivePage


class ReadyProfilePage(ReadyLivePage):
    """ Class: ReadyProfilePage """
    region = '[data-test-id="AccountTabContents-organization"]'
    email_address = '[data-test-id="AccountTabContents-contact-email"]'
    first_name = '#firstName'
    last_name = '#lastName'
    job_title = '#jobTitle'
    save_changes = 'div:nth-child(2) > button'
    snackbar_message = '[data-test-id="SnackbarMsg-text"]'
    en_missing_required_fname = 'div:nth-child(1) > div > div.c-input-assistivetext.empty--invalid'
    en_missing_required_lname = 'div:nth-child(2) > div > div.c-input-assistivetext.empty--invalid'
    jp_missing_required_fname = 'div:nth-child(2) > div > div.c-input-assistivetext.empty--invalid'
    jp_missing_required_lname = 'div:nth-child(1) > div > div.c-input-assistivetext.empty--invalid'

    def verify_profile(self):
        """ Method: verify_profile """
        try:
            self.profile_header = self.get_text(ReadyProfilePage.dashboard_header)
            print("Got profile header: {}".format(self.profile_header))
            actual_region = self.get_text(ReadyProfilePage.region)
            print("Got region: {}".format(actual_region))
            actual_email = self.get_text(ReadyProfilePage.email_address)
            print("Got profile email account: {}".format(actual_email))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to verify profile due to:" + str(error))

    def enter_firstname(self, firstname):
        """ Method: enter_firstname """
        try:
            current_firstname = self.get_input_value(ReadyProfilePage.first_name)
            print("Current first name: {}".format(current_firstname))
            for _ in range(0, len(current_firstname)):
                self.driver.find_element_by_css_selector(ReadyProfilePage.first_name).send_keys(Keys.BACK_SPACE)
            self.enter_text(ReadyProfilePage.first_name, firstname)
            print("Enter first name: {}".format(firstname))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to enter first name due to:" + str(error))

    def enter_lastname(self, lastname):
        """ Method: enter_lastname """
        try:
            current_lastname = self.get_input_value(ReadyProfilePage.last_name)
            print("Current last name: {}".format(current_lastname))
            for _ in range(0, len(current_lastname)):
                self.driver.find_element_by_css_selector(ReadyProfilePage.last_name).send_keys(Keys.BACK_SPACE)
            self.enter_text(ReadyProfilePage.last_name, lastname)
            print("Enter last name: {}".format(lastname))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to enter last name due to:" + str(error))

    def enter_jobtitle(self, jobtitle):
        """ Method: enter_jobtitle """
        try:
            current_title = self.get_input_value(ReadyProfilePage.job_title)
            print("Current job title: {}".format(current_title))
            for _ in range(0, len(current_title)):
                self.driver.find_element_by_css_selector(ReadyProfilePage.job_title).send_keys(Keys.BACK_SPACE)
            if jobtitle != "missing":
                self.enter_text(ReadyProfilePage.job_title, jobtitle)
                print("Entered job title: {}".format(jobtitle))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to enter job title due to:" + str(error))

    def click_save_changes(self):
        """ Method: click_save_changes """
        try:
            self.click_element(ReadyProfilePage.save_changes)
            print("Click Save Changes button!")
            save_msg = self.get_text(ReadyProfilePage.snackbar_message)
            print("Got message: {}".format(save_msg))
            time.sleep(3)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to click Save Changes due to:" + str(error))

    def missing_required(self, firstname, lastname):
        """ Method: missing_firstname """
        try:
            if self.profile_header == "User Profile":
                if firstname == "nofirst":
                    current_firstname = self.get_input_value(ReadyProfilePage.first_name)
                    print("Current first name: {}".format(current_firstname))
                    for _ in range(0, len(current_firstname)):
                        self.driver.find_element_by_css_selector(ReadyProfilePage.first_name).send_keys(Keys.BACK_SPACE)
                    self.click_element(ReadyProfilePage.save_changes)
                    print("Click Save Changes button!")
                    missing_firstname = self.get_text(ReadyProfilePage.en_missing_required_fname)
                    print("Missing required first name: {}".format(missing_firstname))

                if lastname == "nolast":
                    current_lastname =  self.get_input_value(ReadyProfilePage.last_name)
                    print("Current last name: {}".format(current_lastname))
                    for _ in range(0, len(current_lastname)):
                        self.driver.find_element_by_css_selector(ReadyProfilePage.last_name).send_keys(Keys.BACK_SPACE)
                    self.click_element(ReadyProfilePage.save_changes)
                    print("Click Save Changes button!")
                    missing_lastname = self.get_text(ReadyProfilePage.en_missing_required_lname)
                    print("Missing required last name: {}".format(missing_lastname))
            else:
                if firstname == "nofirst":
                    current_firstname = self.get_input_value(ReadyProfilePage.first_name)
                    print("Current first name: {}".format(current_firstname))
                    for _ in range(0, len(current_firstname)):
                        self.driver.find_element_by_css_selector(ReadyProfilePage.first_name).send_keys(Keys.BACK_SPACE)
                    self.click_element(ReadyProfilePage.save_changes)
                    print("Click Save Changes button!")
                    missing_firstname = self.get_text(ReadyProfilePage.jp_missing_required_fname)
                    print("Missing required first name: {}".format(missing_firstname))

                if lastname == "nolast":
                    current_lastname = self.get_input_value(ReadyProfilePage.last_name)
                    print("Current last name: {}".format(current_lastname))
                    for _ in range(0, len(current_lastname)):
                        self.driver.find_element_by_css_selector(ReadyProfilePage.last_name).send_keys(Keys.BACK_SPACE)
                    self.click_element(ReadyProfilePage.save_changes)
                    print("Click Save Changes button!")
                    missing_lastname = self.get_text(ReadyProfilePage.jp_missing_required_lname)
                    print("Missing required last name: {}".format(missing_lastname))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to execute missing required due to:" + str(error))
