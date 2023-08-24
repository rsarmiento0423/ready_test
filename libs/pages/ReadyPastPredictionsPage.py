""" ReadyPastPredictionsPage.py """
#pylint: disable=C0103
#pylint: disable=C0301
#pylint: disable=W0702
#pylint: disable=R0904
#pylint: disable=E0401
import inspect
from selenium.webdriver.common.by import By
from ReadyLivePage import ReadyLivePage


class ReadyPastPredictionsPage(ReadyLivePage):
    """ Class: ReadyPastPredictionsPage """

    first_event = 'a:nth-child(1) > div > div'
    flood_library_card_list = '[data-test-id="library-card-list"] a[data-test-hazard-type="Flood"]'
    pp_card_titles = '[data-test-id="event-title-text"]'
    pp_card_types = '[data-test-id="eventType"]'
    pp_total_impacted_people = '[data-test-id="Stat-numPeople"]'
    pp_total_impacted_buildings = '[data-test-id="Stat-numBuildings"]'
    pp_dates_posted = '[data-test-id="flood-posted-time"]'
    pp_dates_begins = '[data-test-id="flood-start-time"]'
    pp_dates_ends = '[data-test-id="flood-end-time"]'
    return_library_btn = (By.CSS_SELECTOR, '[data-test-id="SidePanelNav-back"]')  #Arrow button on top left after we click seismic card.
    map_display_btn = (By.CSS_SELECTOR, '[data-test-id="SidePanelNav-Layers"]')
    hexagon_slider=(By.CSS_SELECTOR, '.MuiSlider-thumbSizeMedium')
    remove_start_btn = 'button.btn.btn-contained--warning'
    go_back_btn = 'button.btn.btn-text-only--secondary'
    side_panel_river_gauges = '[data-test-id="SidePanelNav-RiverGauges"]'
    pp_event_header = '[data-test-id="EventHeader-name"]'

    def click_first_prediction_card(self):
        """ Method: click_first_prediction_card """
        try:
            self.click_element(ReadyPastPredictionsPage.first_event)
            self.element_present(ReadyPastPredictionsPage.pp_event_header)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to click first prediction card!") from error

    def get_event_header_name(self):
        """ Method: get_event_header_name """
        try:
            event_header_name = self.get_text(ReadyPastPredictionsPage.event_header_name)
            return event_header_name
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get event header name!") from error

    def get_event_header_updated(self):
        """ Method: get_event_header_updated """
        try:
            event_header_updated = self.get_text(ReadyPastPredictionsPage.event_header_updated)
            return event_header_updated
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get event header updated!") from error

    def get_status_overflow_predicted(self):
        """ Method: get_status_overflow_predicted """
        try:
            status_overflow_predicted = self.get_text(ReadyPastPredictionsPage.status_overflow_predicted)
            return status_overflow_predicted
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get status overflow predicted!") from error

    def get_inundated_area(self):
        """ Method: get_inundated_area """
        try:
            inundated_area_message = self.get_inner_text(ReadyPastPredictionsPage.inundated_area)
            return inundated_area_message
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get inundated area!") from error

    def get_total_impact_buildings(self):
        """ Method: get_total_impact_buildings """
        try:
            total_impact_buildings = self.get_inner_text(ReadyPastPredictionsPage.total_impact_buildings2)
            return total_impact_buildings
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get total impact buildings!") from error

    def get_total_impact_people(self):
        """ Method: get_total_impact_people """
        try:
            total_impact_people = self.get_inner_text(ReadyPastPredictionsPage.total_impact_people2)
            return total_impact_people
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get total impact people!") from error

    def check_river_gauge_header(self):
        """ Method: check_river_gauge_header """
        try:
            self.click_element(ReadyPastPredictionsPage.river_gauges_btn)
            river_gauge_status_header = self.get_text(ReadyPastPredictionsPage.river_gauges_header)
            print("Found River Gauges header: {}".format(river_gauge_status_header))
            return river_gauge_status_header
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get river gauges!") from error

    def check_river_gauges_chiba(self):
        """ Method: check_river_gauges_chiba """
        try:
            self.click_element(ReadyPastPredictionsPage.river_gauges_btn)
            actual_river_gauge_status = self.get_inner_text(ReadyPastPredictionsPage.river_gauges_status)
            print("Got river gauge status: {}".format(actual_river_gauge_status))
            assert actual_river_gauge_status in ("Data for river gauge stations is not available at this time.", \
                                                 "No supported river gauges in this region."), \
                                                 "Expected no river gauges found!"
            return 0
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to verify river gauges for Chiba!") from error

    def check_river_gauges(self, expected_total_river_gauges):
        """ Method: check_river_gauges """
        try:
            lst_river_gauge_names = []
            self.click_element(ReadyPastPredictionsPage.river_gauges_btn)
            lst_river_gauges = self.return_object_list(ReadyPastPredictionsPage.river_gauge_name)
            for item in lst_river_gauges:
                print(item.text)
                lst_river_gauge_names.append(item.text)
            actual_total_river_gauges = len(lst_river_gauge_names)
            print("Total river gauges found: {}".format(actual_total_river_gauges))
            assert actual_total_river_gauges == int(expected_total_river_gauges), "Wrong number of river gauges found!"
            return actual_total_river_gauges
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get river gauge name!") from error

    def get_all_past_predictions_urls(self):
        """ Method: get_all_past_predictions_urls """
        try:
            lst_event_urls = self.return_object_list(ReadyPastPredictionsPage.flood_library_card_list)
            print("Total flood events found:", len(lst_event_urls))
            assert len(lst_event_urls) > 0, "No flood events found!"
            for url in lst_event_urls:
                str_url = str(url.get_attribute("href"))
                print("Flood event URL: " + str_url)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get all flood predictions!") from error

    def verify_expected_geo(self, expect_geo):
        """ Method: verify_expected_geo """
        try:
            lst_event_urls = self.return_object_list(ReadyPastPredictionsPage.flood_library_card_list)
            print("Total flood events found:", len(lst_event_urls))
            assert len(lst_event_urls) > 0, "No flood events found!"
            iCount = 0
            for url in lst_event_urls:
                str_url = str(url.get_attribute("href"))
                print("Flood event URL: " + str_url)
                if not str_url.endswith(expect_geo):
                    iCount += 1
            assert iCount == 0, "Found unexpected geo in Past Predictions!"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError(f"Fail to verify expected geo: {expect_geo}!") from error

    def get_all_prediction_cards_titles(self):
        """ Method: get_all_prediction_cards_titles """
        try:
            lst_event_titles_pp = self.return_object_list(ReadyPastPredictionsPage.pp_card_titles)
            assert len(lst_event_titles_pp) > 0, "No Past Predictions found!"
            for title in lst_event_titles_pp:
                print("Flood Title: {}".format(title.get_attribute("innerHTML")))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get all flood prediction card titles!") from error

    def get_all_prediction_cards_types(self):
        """ Method: get_all_prediction_cards_types """
        try:
            lst_event_types_pp = self.return_object_list(ReadyPastPredictionsPage.pp_card_types)
            assert len(lst_event_types_pp) > 0, "No Past Predictions found!"
            for event_type in lst_event_types_pp:
                print("Flood Type:{}".format(event_type.get_attribute("innerHTML")))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get all flood prediction card types!") from error

    def get_all_prediction_cards_total_impacted_people(self):
        """ Method: get_all_prediction_cards_total_impacted_people """
        try:
            lst_total_impacted_people_pp = self.return_object_list(ReadyPastPredictionsPage.pp_total_impacted_people)
            assert len(lst_total_impacted_people_pp) > 0, "No Past Predictions found!"
            for tot_people in lst_total_impacted_people_pp:
                print("Total impacted people: {}".format(tot_people.get_attribute("innerHTML")))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get total impacted people!") from error

    def get_all_prediction_cards_total_impacted_buildings(self):
        """ Method: get_all_prediction_cards_total_impacted_buildings """
        try:
            lst_total_impacted_buildings_pp = self.return_object_list(ReadyPastPredictionsPage.pp_total_impacted_buildings)
            assert len(lst_total_impacted_buildings_pp) > 0, "No Past Predictions found!"
            for tot_buildings in lst_total_impacted_buildings_pp:
                print("Total impacted buildings: {}".format(tot_buildings.get_attribute("innerHTML")))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get total impacted buildings!") from error

    def get_all_prediction_cards_date_posted(self):
        """ Method: get_all_prediction_cards_date_posted """
        try:
            lst_dates_posted_pp = self.return_object_list(ReadyPastPredictionsPage.pp_dates_posted)
            assert len(lst_dates_posted_pp) > 0, "No Past Predictions found!"
            for date_posted in lst_dates_posted_pp:
                print("Date Posted: {}".format(date_posted.get_attribute("innerHTML")))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get date posted!") from error

    def get_all_prediction_cards_date_prediction_begins(self):
        """ Method: get_all_prediction_cards_date_prediction_begins """
        try:
            lst_dates_prediction_begins_pp = self.return_object_list(ReadyPastPredictionsPage.pp_dates_begins)
            assert len(lst_dates_prediction_begins_pp) > 0, "No Past Predictions found!"
            for date_prediction_begins in lst_dates_prediction_begins_pp:
                print("Date Prediction Begins: {}".format(date_prediction_begins.get_attribute("innerHTML")))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get date prediction begins!") from error

    def get_all_prediction_cards_date_prediction_ends(self):
        """ Method: get_all_prediction_cards_date_prediction_ends """
        try:
            lst_dates_prediction_ends_pp = self.return_object_list(ReadyPastPredictionsPage.pp_dates_ends)
            assert len(lst_dates_prediction_ends_pp) > 0, "No Past Predictions found!"
            for date_prediction_ends in lst_dates_prediction_ends_pp:
                print("Date Prediction Begins: {}".format(date_prediction_ends.get_attribute("innerHTML")))
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get date prediction begins!") from error

    def toggle_star_prediction(self):
        """ Method: toggle_star_prediction """
        self.click_element(ReadyPastPredictionsPage.star_prediction_toggle)
        try:
            self.element_present(ReadyPastPredictionsPage.remove_start_btn)
            self.click_element(ReadyPastPredictionsPage.remove_start_btn)
            print("Clicked Remove Star button.")
        except:
            try:
                status = self.get_class_attribute(ReadyPastPredictionsPage.star_prediction_value)
                print("Got status: {}".format(status))
                self.click_element(ReadyPastPredictionsPage.star_prediction_toggle)
                status = self.get_class_attribute(ReadyPastPredictionsPage.star_prediction_value)
                print("Got status: {}".format(status))
            except Exception as error:
                self.generate_screenshot(inspect.stack()[0][3] + "_error")
                raise RuntimeError("Fail to toggle star prediction!") from error

    def click_nav_layers(self):
        """ Method: click_nav_layers """
        try:
            self.click_element(ReadyPastPredictionsPage.nav_layers)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click nav layers icon!") from error

    def click_velocity_arrows(self):
        """ Method: click_velocity_arrows """
        try:
            self.click_element(ReadyPastPredictionsPage.velocity_arrows)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click velocity arrows checkbox!") from error

    def click_all_shelters(self):
        """ Method: click_all_shelters """
        try:
            self.click_element(ReadyPastPredictionsPage.choose_all_shelters)
            self.generate_screenshot(inspect.stack()[0][3] + "_all_shelters")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to select all shelters checkbox!") from error

    def click_show_satellite(self):
        """ Method: click_show_satellite """
        try:
            self.click_element(ReadyPastPredictionsPage.show_satellite)
            self.generate_screenshot(inspect.stack()[0][3] + "_satellite_map")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click satellite map radio button!") from error

    def click_impact_map(self):
        """ Method: click_impact_map """
        try:
            self.click_element(ReadyPastPredictionsPage.impact_map_display)
            self.generate_screenshot(inspect.stack()[0][3] + "_impact_map")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click impact map radio button!") from error

    def click_show_map(self):
        """ Method: click_show_map """
        try:
            self.click_element(ReadyPastPredictionsPage.show_map)
            self.generate_screenshot(inspect.stack()[0][3] + "_show_map")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click map radio button!") from error

    def click_flood_normal_map(self):
        """ Method: click_flood_normal_map """
        try:
            self.click_element(ReadyPastPredictionsPage.flood_normal_map)
            self.generate_screenshot(inspect.stack()[0][3] + "_flood_map")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click flood map radio button!") from error

    def click_basic_shelters(self):
        """ Method: click_basic_shelters """
        try:
            self.click_element(ReadyPastPredictionsPage.basic_shelters,3)
            self.generate_screenshot(inspect.stack()[0][3] + "_basic_shelters")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click basic shelters checkbox!") from error

    def click_short_term_shelters(self):
        """ Method: click_short_term_shelters """
        try:
            self.click_element(ReadyPastPredictionsPage.short_term_shelters)
            self.generate_screenshot(inspect.stack()[0][3] + "_short_term_shelters")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click short term shelters checkbox!") from error

    def click_wide_area_shelters(self):
        """ Method: click_wide_area_shelters """
        try:
            self.click_element(ReadyPastPredictionsPage.wide_area_shelters)
            self.generate_screenshot(inspect.stack()[0][3] + "_wide_area_shelters")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click wide area shelters checkbox!") from error

    def verify_no_river_gauge_tab(self):
        """ Method: verify_no_river_gauge_tab """
        try:
            if self.element_not_present(ReadyPastPredictionsPage.side_panel_river_gauges):
                print("PASS: No river gauge tab found as expected!")
            else:
                raise Exception("FAIL: Found unexpected river gauge tab!")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to verify no river gauge tab is present!") from error
