""" ReadyLibraryPage.py """
# pylint: disable=C0301
# pylint: disable=C0103
# pylint: disable=W0707
# pylint: disable=W0401
# pylint: disable=R0904
# pylint: disable=W0614
# pylint: disable=W0201

import inspect
import time

from ReadyLivePage import ReadyLivePage


class ReadyHelpPage(ReadyLivePage):
    """Class: ReadyProfilePage"""

    header_welcome_txt = ".header__headline"
    article_search_field = ".search__input.js__search-input.o__ltr"
    result_search_article = ".paper__preview.c__body"
    intercomm_msg_frame = "intercom-messenger-frame"
    intercom_start_msg_btn = ".intercom-lightweight-app-launcher.intercom-launcher"
    intercom_send_msg_btn = ".intercom-18biwo.e1prtmiu1"
    intercom_return_from_send_msg_arrow = (
        ".intercom-messenger-header-buttons-back-button.intercom-18r30ow.e40f3ct0"
    )
    intercom_close_btn_frame = "intercom-launcher-frame"
    intercom_close_frame_btn = ".intercom-1f2urc1.e4nbtsn3"
    footer_facebook = ".footer__link.footer__link__facebook"
    footer_twitter = ".footer__link.footer__link__twitter"
    footer_linkedin = ".footer__link.footer__link__linkedin"
    help_btn = (
        '[data-test-id="ProductDashboardMenu-DashboardMenu-DashboardMenuOption-help"]'
    )

    def verify_help_page(self):
        """Method:  verify_help_page"""
        try:
            header_txt = self.get_text(ReadyHelpPage.header_welcome_txt)
            assert "Advice and answers from the One Concern Team" in header_txt
            page_title = self.driver.title
            assert page_title == "One Concern Help Center"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to verify Help Page objects due to:" + str(error))

    def search_for_article_name(self, article_name):
        """Method:  search_for_article_name"""
        try:
            self.enter_text(ReadyHelpPage.article_search_field, article_name)
            self.send_enter_key(ReadyHelpPage.article_search_field, "ENTER")
            time.sleep(1)
            result_text = self.get_text(ReadyHelpPage.result_search_article)
            assert article_name in result_text
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to verify search for article due to:" + str(error))

    def validate_actions_on_intercom_msg(self):
        """Method:  validate_actions_on_intercom_msg"""
        try:
            time.sleep(2)
            self.click_element(ReadyHelpPage.intercom_start_msg_btn)
            self.driver.switch_to.frame(ReadyHelpPage.intercomm_msg_frame)
            self.click_element(ReadyHelpPage.intercom_send_msg_btn)
            self.click_element(ReadyHelpPage.intercom_return_from_send_msg_arrow)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(ReadyHelpPage.intercom_close_btn_frame)
            self.click_element(ReadyHelpPage.intercom_close_frame_btn)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to open the intercom msg due to:" + str(error))

    def validate_footer_social_links(self):
        """Method:  validate_footer_social_links"""
        try:
            self.click_element(".footer__link.footer__link__facebook")
            time.sleep(2)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[2])
            assert "One Concern | Facebook" in self.driver.title
            self.driver.close()
            time.sleep(2)
            self.driver.switch_to.window(handles[1])
            self.click_element(".footer__link.footer__link__twitter")
            time.sleep(2)
            assert len(self.driver.window_handles) == 3
            self.driver.switch_to.window(handles[1])
            self.click_element(ReadyHelpPage.footer_linkedin)
            time.sleep(2)
            assert len(self.driver.window_handles) == 4
            self.driver.switch_to.window(handles[1])

        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise Exception("Fail to open the social links due to:" + str(error))
