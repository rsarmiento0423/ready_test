""" ReadyPredictionsPage.py """

import time
from ReadyLivePage import ReadyLivePage
from ReadyLibraryPage import ReadyLibraryPage
from ReadyPastPredictionsPage import ReadyPastPredictionsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ReadyPredictionsPage(ReadyPastPredictionsPage,ReadyLibraryPage,ReadyLivePage):
    """ Class: ReadyPredictionsPage """

    first_event = (By.CSS_SELECTOR, 'a:nth-child(1) > div > div')
    flood_library_card_list = (By.CSS_SELECTOR, 'div[data-test-id=["library-card-list"] a[data-test-hazard-type="Flood"]')
    #map_display_btn = (By.XPATH, '//nav[contains(@class,"o-flex-vcenter-container")]//div[3]')
    hexagon_slider = (By.XPATH, '//span[contains(@class, "MuiSlider-thumbSizeMedium")]')
    return_library_btn = (By.CSS_SELECTOR, '[data-test-id="SidePanelNav-back"]')  #Arrow button on top left after we click seismic card.



    def click_all_shelters(self):
        """ Method: click_all_shelters """
        try:
            self.click_element(ReadyPredictionsPage.choose_all_shelters)
            time.sleep(0.5)
        except Exception as e:
            raise Exception("Fail to select all shelters checkbox due to: {}" + str(e))

    def click_show_satellite(self):
        """ Method: click_show_satellite """
        try:
            self.click_element(ReadyPredictionsPage.show_satellite)
            time.sleep(5)
        except Exception as e:
            raise Exception("Fail to click satellite map radio button due to: {}" + str(e))

    def click_show_map(self):
        """ Method: click_show_map """
        try:
            self.click_element(ReadyPredictionsPage.show_map)
            time.sleep(0.5)
        except Exception as e:
            raise Exception("Fail to click map radio button due to: {}" + str(e))


    def click_basic_shelters(self):
        """ Method: click_basic_shelters """
        try:
            self.click_element(ReadyPredictionsPage.basic_shelters)
            time.sleep(0.5)
        except Exception as e:
            raise Exception("Fail to click basic shelters checkbox due to: {}" + str(e))

    def click_short_term_shelters(self):
        """ Method: click_short_term_shelters """
        try:
            self.click_element(ReadyPredictionsPage.short_term_shelters)
            time.sleep(0.5)
        except Exception as e:
            raise Exception("Fail to click short term shelters checkbox due to: {}" + str(e))

    def click_wide_area_shelters(self):
        """ Method: click_wide_area_shelters """
        try:
            self.click_element(ReadyPredictionsPage.wide_area_shelters)
            time.sleep(0.5)
        except Exception as e:
            raise Exception("Fail to click wide area shelters checkbox due to: {}" + str(e))

    def return_from_seismic_card(self):
        """ Method: return_from_seismic_card """
        try:
            self.driver.find_element(*ReadyPredictionsPage.return_library_btn).click()
        except Exception as e:
            raise Exception("Couldn't return due to: {}" + str(e))

    def slide_hexagon_opacity(self):
        """ Method: slide_hexagon_opacity """
        slider = self.driver.find_element(*ReadyPredictionsPage.hexagon_slider)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(slider,338,178).perform()
        slider_style = slider.get_attribute("style")
        slider_should_be = "left: 100%;"
        if slider_style == slider_should_be:
            pass
        else:
            raise Exception("Slider style not correct")

    def click_map_display(self):
        """ Method: click_map_display """
        try:
            # self.driver.find_element(*ReadyPredictionsPage.map_display_btn).click()  # For XPATH
            self.driver.find_element(*ReadyPredictionsPage.map_display_btn).click()
            time.sleep(0.5)
        except Exception as e:
            raise Exception("Couldnt click the map display due to: {}" + str(e))
