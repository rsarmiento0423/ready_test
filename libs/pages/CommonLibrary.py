""" CommonLibrary.py """
# pylint: disable=R0915
# pylint: disable=E0001

import json
import os.path
import time
from datetime import datetime

from robot.api import logger
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CommonLibrary:
    """Class: CommonLibrary"""

    def __init__(self, envfile, browser, url):
        """
        Create the variables associated with the class
        :type envfile: string
        :param envfile: the environment JSON file

        :type browser: string
        :param browser: can be chrome, firefox, or msedge

        :type url: string
        :param url: should be a valid url to Ready staging or production
        """

        self.url = url
        self.max_browser_wait = 30
        self.wait_for_obj = 20
        self.seismic_event_found = False
        self.flood_event_found = False
        try:
            if self.url not in [
                "https://app.staging.onec.co/#/",
                "https://app.oneconcern.com/#/",
            ]:
                raise Exception(
                    "Aborting testing due to URL: {} does not exist!".format(url)
                )

            envfile_path = "./data/" + envfile
            if os.path.exists(envfile_path):
                with open(envfile_path) as json_file:
                    self.data = json.load(json_file)
            else:
                raise Exception(
                    "Aborting testing due to environment file: {} does not exist!".format(
                        envfile_path
                    )
                )

            if browser.lower() == "chrome":
                print("Running against Chrome browser...")
                options = webdriver.ChromeOptions()
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--start-maximized")
                options.add_argument("--headless")
                # The line below checks for the version of the browser.
                # We need to get the error and print, otherwise we only see the error in debug mode.
                self.driver = webdriver.Chrome(
                    executable_path="/usr/local/bin/chromedriver", options=options
                )
                locale = {
                    "staging": "https://auth.staging.onec.co/auth/realms/oneconcern/login-actions/authenticate?kc_locale=en",
                    "prod": "https://auth.oneconcern.com/auth/realms/oneconcern/login-actions/authenticate?kc_locale=en",
                }
                if "staging" in self.url:
                    print("Setting staging to EN locale!")
                    self.driver.get(locale["staging"])
                else:
                    print("Setting production to EN locale!")
                    self.driver.get(locale["prod"])
                self.driver.get(self.url)
                self.driver.implicitly_wait(self.max_browser_wait)
                page_title = self.driver.title
                print("Login Page title: {}".format(page_title))
                assert (
                    page_title == "One Concern"
                ), "Expected 'One Concern' for page title!"

            if browser.lower() == "firefox":
                print("Running against Firefox browser...")
                options = webdriver.FirefoxOptions()
                options.add_argument("--headless")
                self.driver = webdriver.Firefox(
                    executable_path="/usr/local/bin/geckodriver", options=options
                )
                locale = "https://auth.staging.onec.co/auth/realms/oneconcern/login-actions/authenticate?kc_locale=en"
                if "staging" in self.url:
                    print("Setting to EN locale!")
                    self.driver.get(locale)
                self.driver.get(self.url)
                self.driver.implicitly_wait(self.max_browser_wait)
                pagetitle = self.driver.title
                print("Login Page title: {}".format(pagetitle))
                assert (
                    pagetitle == "One Concern"
                ), "Expected 'One Concern' for page title!"

            if browser.lower() == "edge":
                print("Running against MS Edge browser...")
                options = webdriver.EdgeOptions()
                options.use_chromium = True
                options.add_argument("--headless")
                self.driver = webdriver.Edge(
                    executable_path="/usr/local/bin/msedgedriver", options=options
                )
                locale = "https://auth.staging.onec.co/auth/realms/oneconcern/login-actions/authenticate?kc_locale=en"
                if "staging" in self.url:
                    print("Setting to EN locale!")
                    self.driver.get(locale)
                self.driver.get(self.url)
                self.driver.implicitly_wait(self.max_browser_wait)
                pagetitle = self.driver.title
                print("Login Page title: {}".format(pagetitle))
                assert (
                    pagetitle == "One Concern"
                ), "Expected 'One Concern' for page title!"

            if browser.lower() not in ["chrome", "firefox", "edge"]:
                raise Exception(
                    "Browser: {} is currently not supported!".format(browser)
                )
        except Exception as error:
            raise RuntimeError("Failure to access URL: {}".format(url)) from error

    @staticmethod
    def get_date_time():
        """Method: get_date_time"""
        timestamp = time.strftime("%m%d%Y%H%M%S")
        return timestamp

    def enter_text(self, myobject, myinput):
        """Method: enter_text
        :type myobject: string
        :param myobject: the proper CSS Selector

        :type myinput: string
        :param myinput: the string value to be entered
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, myobject))
            )
            element.send_keys(str(myinput))
        except NoSuchElementException as error:
            raise RuntimeError(
                f"Failed to enter text in element: {myobject}"
            ) from error

    def click_element(self, theobject, pause=0):
        """Method: click_element
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        :type pause: int
        :param pause: this is delay in seconds after clicking element
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            element.click()
            time.sleep(pause)
        except NoSuchElementException as error:
            raise RuntimeError(f"Failed to click element: {theobject}") from error

    def element_present(self, theobject):
        """Method: element_present
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            if not element.is_displayed():
                raise Exception(f"Expected element: {theobject} to be present!")
            return True
        except NoSuchElementException as error:
            raise RuntimeError(
                f"Failed to verify element is present: {theobject}"
            ) from error

    def element_not_present(self, theobject):
        """Method: element_not_present
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return True
        except NoSuchElementException:
            print("Element not present as expected!")
            return False

    def get_text(self, theobject):
        """Method: get_text
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return element.text
        except NoSuchElementException as error:
            raise RuntimeError(f"Failed get text: {theobject}:") from error

    def get_inner_text(self, theobject):
        """Method: get_inner_text
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return element.get_attribute("innerHTML")
        except NoSuchElementException as error:
            raise RuntimeError(f"Failed get inner text: {theobject}:") from error

    def get_class_attribute(self, theobject):
        """Method: get_class_attribute
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return element.get_attribute("class")
        except NoSuchElementException as error:
            raise RuntimeError(f"Failed get class: {theobject}:") from error

    def get_input_value(self, theobject):
        """Method: get_input_value
        :type theobject: string
        :param theobject: the CSS Selector for the page object
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, theobject))
            )
            return element.get_attribute("value")
        except NoSuchElementException as error:
            raise RuntimeError(f"Failed get input value: {theobject}:") from error

    def return_object_list(self, objects):
        """Method: get_object_list
        :type objects: string
        :param objects: the CSS Selector for the list of page objects
        """
        try:
            lst_objects = self.driver.find_elements(By.CSS_SELECTOR, objects)
            return lst_objects
        except NoSuchElementException as error:
            raise RuntimeError(f"Failed to return object list: {objects}") from error

    def generate_screenshot(self, error_file_name):
        """Method: generate_screenshot
        :type error_file_name: string
        :param error_file_name: this is the file name
        """
        screenshot = str(error_file_name) + "_" + self.get_date_time() + ".png"
        self.driver.save_screenshot(screenshot)
        print(f"Generated screenshot: {screenshot}")
        logger.info(
            "<img src='" + str(screenshot) + "' width='1400' height='900'/>", html=True
        )

    def clear_field(self, field):
        """Method: clear_field
        :type field: string
        :param field: the proper CSS Selector
        """
        try:
            element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, field))
            )
            element.clear()
        except NoSuchElementException as error:
            raise RuntimeError(f"Failed to clear field: {field}") from error

    @staticmethod
    def get_total_duration(start, end, verify="skip"):
        """Method: get_total_duration
        :type start: string
        :param start: the start time in Numeric Month-Day Hour:Min
        :type end: string
        :param end: the start time in Numeric Month-Day Hour:Min
        :type verify: string
        :param verify: default skip or prod
        """
        dt_object1 = datetime.strptime(start, "%m-%d %H:%M")
        dt_object2 = datetime.strptime(end, "%m-%d %H:%M")
        delta = dt_object2 - dt_object1
        sec = delta.total_seconds()
        hours = sec / (60 * 60)
        print(f"Flood duration in hours: {hours}")
        if verify == "prod":
            assert hours == 36.0, "Expected flood duration for 36 hours!"
        else:
            assert hours in (
                3.0,
                36.0,
            ), "Expected flood duration should be either 3 hours or 36 hours!"

    @staticmethod
    def verify_3hr_intervals(start, end):
        """Method: verify_3hr_intervals
        :type start: string
        :param start: the start time in Month Day, Year Hour:Min
        :type end: string
        :param end: the start time in Month Day, Year Hour:Min
        """
        dt_object1 = datetime.strptime(start, "%B %d, %Y %H:%M")
        dt_object2 = datetime.strptime(end, "%B %d, %Y %H:%M")
        delta = dt_object2 - dt_object1
        sec = delta.total_seconds()
        hours = sec / (60 * 60)
        print(f"Flood interval in hours: {hours}")
        assert hours == 3.0, "Expected 3 hours flood interval!"

    @staticmethod
    def pause(delay=1):
        """Method: pause
        :type delay: int
        :param delay: for pausing test execution
        """
        time.sleep(delay)

    def send_enter_key(self, elem, keys):
        """Method: send_enter_key
        :type elem: WebDriver Element
        :param elem: The locator for the element on the web
        :type keys: keyboard.ENTER.keys
        :param keys: Keys that user wants to send. ex Keys.ENTER
        """
        try:
            Element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, elem))
            )
            Element.send_keys(Keys.ENTER)
        except NoSuchElementException as error:
            raise RuntimeError(
                f"Failed to send keys {keys} in element: {elem}"
            ) from error

    def send_end_key(self, elem, keys):
        """Method: send_end_key
        :type elem: WebDriver Element
        :param elem: The locator for the element on the web
        :type keys: keyboard.END.keys
        :param keys: Keys that user wants to send. ex Keys.ENTER
        """
        try:
            Element = WebDriverWait(self.driver, self.wait_for_obj).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, elem))
            )
            Element.send_keys(Keys.PAGE_DOWN)
        except NoSuchElementException as error:
            raise RuntimeError(
                f"Failed to send keys {keys} in element: {elem}"
            ) from error
