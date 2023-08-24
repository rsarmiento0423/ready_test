""" ReadyLivePage.py """
import inspect

from ReadyLoginPage import ReadyLoginPage


class ReadyLivePage(ReadyLoginPage):
    """Class: ReadyLivePage"""

    dashboard_live = (
        '[data-test-id="ProductDashboardMenu-DashboardMenu-DashboardMenuOption-live"]'
    )
    dashboard_past_river_gauge_predictions = '[data-test-id="ProductDashboardMenu-DashboardMenu-DashboardMenuOption-pastRiverGagues"]'
    dashboard_past_predictions = '[data-test-id="ProductDashboardMenu-DashboardMenu-DashboardMenuOption-pastPredictions"]'
    dashboard_library = '[data-test-id="ProductDashboardMenu-DashboardMenu-DashboardMenuOption-library"]'
    dashboard_profile = 'div[data-test-id="ProductDashboardMenu-DashboardMenu-DashboardMenuOption-profile"]'
    dashboard_help = (
        '[data-test-id="ProductDashboardMenu-DashboardMenu-DashboardMenuOption-help"]'
    )
    dashboard_terms_conditions = (
        '[data-test-id="ProductDashboardMenu-DashboardMenu-DashboardMenuOption-terms"]'
    )
    dashboard_header = '[data-test-id="RouteTitle"]'
    dashboard_hazard_chip = '[data-test-id="HazardChip"] > span'
    dashboard_map = ".mapboxgl-map canvas"
    dashboard_hazard = '[data-test-id="HazardChip"] > span.u-background-red'
    dashboard_no_hazard = '[data-test-id="HazardChip"] > span.u-background-green'
    no_hazard_message = '[data-test-id="ImpactCard-blurb-green"]'
    event_header_name = '[data-test-id="EventHeader-name"]'
    event_header_updated = '[data-test-id="EventHeader-updated"]'

    ### Seismic
    time_of_earthquake = '[data-test-id="SeismicInfo"] > [data-test-id="startTime"] > [data-test-id="value"]'
    magnitude = '[data-test-id="magnitude"] > [data-test-id="value"]'
    location = '[data-test-id="location"] > [data-test-id="value"]'
    epicenter = '[data-test-id="epicenter"] > [data-test-id="value"]'
    depth = '[data-test-id="earthquakeDepth"] > [data-test-id="value"]'
    total_impact_buildings = '[data-test-id="StatsTable-impactedBuildings"] > [data-test-id2="StatsRow-total"] > [data-test-id="value"]'
    total_impact_people = '[data-test-id="StatsTable-impactedPeople"] > [data-test-id2="StatsRow-total"] > [data-test-id="value"]'
    seismic_view_prediction_btn = '[data-test-hazard-type="Seismic"] button'
    list_event_titles = '[data-test-id="event-title-text"]'
    list_total_impacted_people = (
        '[data-test-id="EventOverallStats-people-Stat-numPeople"]'
    )
    list_total_impacted_buildings = (
        '[data-test-id="EventOverallStats-buildings-Stat-numBuildings"]'
    )
    list_earthquake_times = (
        '[data-test-hazard-type="Seismic"] > [data-test-id="startTime"]'
    )
    list_earthquake_magnitudes = '[data-test-id="magnitude"]'
    list_earthquake_locations = '[data-test-id="location"]'
    list_earthquake_epicenters = '[data-test-id="epicenter"]'
    list_earthquake_depths = '[data-test-id="earthquakeDepth"]'

    ### Flood
    flood_view_prediction_btn = (
        '[data-test-hazard-type="Flood"] div:nth-child(1) > button'
    )
    river_gauges_btn = (
        '[data-test-id="SidePanelNav-RiverGauges"] div[class="c-navbutton"]'
    )
    river_gauges_status = '[data-test-id="SidePanelTabContent-Card"] div[class="f-grey u-marginy--10 u-padding--10 u-aligncenter"]'
    river_gauge_name = '[data-test-id="gaugeName"]'
    river_gauges_header = '[data-test-id="riverGaugesTabTitle"]'
    river_gauge_chart = '[data-test-id="RiverGaugeChart-Card"]'
    river_gauge_address = '[data-test-id="gaugeAddress"]'
    river_system = '[data-test-id="riverSystem"]'
    river_name = '[data-test-id="riverName"]'
    river_threshold_reached_list = '[data-test-id="ThresholdReachedList"]'
    river_threshold_legend_text = '[data-test-id="threshLegendText"]'
    status_overflow_predicted = '[data-test-id="noOverflowPredicted"]'
    inundated_area = '[data-test-id="StatsRow-inundatedArea"] [data-test-id="value"]'
    total_impact_buildings1 = '[data-test-id="StatsTable-impactedBuildings"]  [data-test-id2="StatsRow-total"] [data-test-id="value"]'
    total_impact_buildings2 = '[data-test-id="StatsTable-impactedBuildings"]  [data-test-id2="StatsRow-total"] [data-test-id="value"]'
    total_impact_people1 = '[data-test-id="StatsTable-impactedPeople"] [data-test-id2="StatsRow-total"] [data-test-id="value"]'
    total_impact_people2 = '[data-test-id="StatsTable-impactedPeople"] [data-test-id2="StatsRow-total"] [data-test-id="value"]'
    star_prediction_toggle = '[data-test-id="StarPredictionToggle"]'
    star_prediction_value = '[data-test-id="StarPredictionToggle"] > i'
    play_button = "#js-TimelinePlay"
    nav_layers = '[data-test-id="SidePanelNav-Layers"] > div.c-navbutton'
    flood_normal_map = 'input[value="FloodNormal"]'
    impact_map_display = 'input[value="FloodImpact"]'
    show_map = 'input[value="showMap"]'
    show_satellite = 'input[value="showSatellite"]'
    velocity_arrows = "#checkbox-velocity-arrows"
    choose_all_shelters = "#shelters"
    basic_shelters = "#Type1"
    short_term_shelters = "#Type2"
    wide_area_shelters = "#Type3"
    alert_panel_title = '[data-test-id="alertPanelTitle"]'
    flood_depth_2_to_6_in = '[data-test-id="StatsRow-2 - 6 in"] [data-test-id="value"]'
    flood_depth_6in_to_1ft = (
        '[data-test-id="StatsRow-6 in - 1 ft"] [data-test-id="value"]'
    )
    flood_depth_1_to_2ft = '[data-test-id="StatsRow-1 - 2 ft"] [data-test-id="value"]'
    flood_depth_2_to_3ft = '[data-test-id="StatsRow-2 - 3 ft"] [data-test-id="value"]'
    flood_depth_3_to_4ft = '[data-test-id="StatsRow-3 - 4 ft"] [data-test-id="value"]'
    flood_depth_4_to_5ft = '[data-test-id="StatsRow-4 - 5 ft"] [data-test-id="value"]'
    flood_depth_5_to_6ft = '[data-test-id="StatsRow-5 - 6 ft"] [data-test-id="value"]'
    flood_depth_greater_6ft = '[data-test-id="StatsRow-> 6 ft"] [data-test-id="value"]'

    ### River Gauge
    posted = '[data-test-id="postedAt"]'
    weather_forecast_time = '[data-test-id="weatherForecastTime"]'
    max_1hr_rainfall = '[data-test-id="rainfallHourly"]'
    max_24hr_rainfall = '[data-test-id="rainfallDaily"]'
    river_gauge_card = '[data-test-id="RiverGaugeRunItem-Card"]'
    past_river_gauge_blocks = '[data-test-id="PastGaugesList"] > div'
    past_river_gauge_headers = '[data-test-id="PastGaugesList"] > div > div'
    first_past_river_gauge_prediction = "section > div:nth-child(1) > div > div"
    view_mlit_links = '[data-test-id="viewLinkMLIT"]'
    no_live_river_gauge_predictions_available = (
        '[data-test-id="RiverGaugeRunCard-Empty-Card"]'
    )
    river_gauge_names = '[data-test-id="gaugeName"]'
    river_gauge_chart_card = '[data-test-id="RiverGaugeChart-Card"]'
    units_meters = "div > svg > g:nth-child(7) > text > tspan"
    graph_start_time = "div > svg > g:nth-child(4) > text > tspan"
    graph_end_time = "div > svg > g:nth-child(5) > text > tspan"
    threshold_chart_legend = '[data-test-id="ThresholdChartLegend"]'
    no_stats_message = '[data-test-id="NoStatsMessage"]'
    threshold_reached_list = '[data-test-id="ThresholdReachedList"]'
    threshold_level_2 = '[data-test-id="threshold-lvl-2"]'
    threshold_level_3 = '[data-test-id="threshold-lvl-3"]'
    threshold_level_2_text = (
        '[data-test-id="threshold-lvl-2"] [data-test-id="threshLegendText"]'
    )
    threshold_level_3_text = (
        '[data-test-id="threshold-lvl-3"] [data-test-id="threshLegendText"]'
    )

    def click_live(self):
        """Method: click_live"""
        try:
            self.click_element(ReadyLivePage.dashboard_live)
            live_header = self.get_text(ReadyLivePage.dashboard_header)
            assert live_header in ("Live", "ホーム"), "Wrong header for Live!"
        except Exception as error:
            raise RuntimeError("Fail to click Live!") from error

    def click_past_river_gauge_predictions(self):
        """Method: click_past_river_gauge_predictions"""
        try:
            self.click_element(ReadyLivePage.dashboard_past_river_gauge_predictions)
            past_river_gauge_predictions_header = self.get_text(
                ReadyLivePage.dashboard_header
            )
            assert past_river_gauge_predictions_header in (
                "Past River Gauge Predictions",
                "河川水位予測履歴",
            ), "Wrong header for Past River Gauge Predictions!"
        except Exception as error:
            raise RuntimeError("Fail to click Past River Gauge Predictions!") from error

    def click_past_predictions(self):
        """Method: click_past_predictions"""
        try:
            self.click_element(ReadyLivePage.dashboard_past_predictions)
            past_predictions_header = self.get_text(ReadyLivePage.dashboard_header)
            assert past_predictions_header in (
                "Past Predictions",
                "予測履歴",
            ), "Wrong header for Past Predictions!"
        except Exception as error:
            raise RuntimeError("Fail to click Past Predictions!") from error

    def click_library(self):
        """Method: click_library"""
        try:
            self.click_element(ReadyLivePage.dashboard_library)
            library_header = self.get_text(ReadyLivePage.dashboard_header)
            print("Got library header: {}".format(library_header))
            assert library_header in ("Library", "ライブラリ"), "Wrong header for Library!"
        except Exception as error:
            raise RuntimeError("Fail to click Library!") from error

    def click_profile(self):
        """Method: click_profile"""
        try:
            self.click_element(ReadyLivePage.dashboard_profile)
            profile_header = self.get_text(ReadyLivePage.dashboard_header)
            print("Got profile header: {}".format(profile_header))
            assert profile_header in (
                "User Profile",
                "ユーザープロフィール",
            ), "Wrong header for 'User Profile'!"
        except Exception as error:
            raise RuntimeError("Fail to click Profile!") from error

    def click_help(self):
        """Method: click_help"""
        try:
            self.click_element(ReadyLivePage.dashboard_help)
            handles = self.driver.window_handles
            size = len(handles)
            if size > 1:
                self.driver.switch_to.window(handles[1])
                help_title = self.driver.title
                print("Got Help title: {}".format(help_title))
            else:
                raise Exception("Unable to launch Help!!!")
        except Exception as error:
            raise RuntimeError("Fail to click Help!") from error

    def click_terms_conditions(self):
        """Method: click_terms_conditions"""
        try:
            self.click_element(ReadyLivePage.dashboard_terms_conditions)
            terms_conditions_header = self.get_text(ReadyLivePage.dashboard_header)
            print("Got Terms and Conditions header: {}".format(terms_conditions_header))
            assert terms_conditions_header in (
                "Terms and Conditions",
                "利用規約",
            ), "Wrong header for 'Terms and Conditions'!"
        except Exception as error:
            self.generate_screenshot("click_terms_and_conditions_error")
            raise RuntimeError("Fail to click Terms and Conditions!") from error

    def verify_blue_sky(self):
        """Method: verify_blue_sky"""
        try:
            detected_hazard = self.get_text(ReadyLivePage.dashboard_hazard_chip)
            if detected_hazard == "No hazards detected":
                print(f"Hazard chip status: {detected_hazard} for Blue Sky!")
                message = self.get_inner_text(ReadyLivePage.no_hazard_message)
                print(f"Got no hazard message: {message}")
                assert (
                    "There is no hazard impact forecast for this area" in message
                ), "No hazard message found!"
                # Verify no flood or seismic events appear for Blue Sky
                self.verify_no_flood_event()
                self.verify_no_seismic_event()
            else:
                print(
                    f"Hazard chip status: {detected_hazard} with Live hazard detected!"
                )
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to verify Blue Sky!") from error

    def get_live_prediction_cards_titles(self):
        """Method: get_live_prediction_cards_titles"""
        try:
            lst_event_titles = self.return_object_list(ReadyLivePage.list_event_titles)
            assert len(lst_event_titles) > 0, "No prediction cards found in Live!"
            for title in lst_event_titles:
                print("Live Event Title: {}".format(title.get_attribute("innerHTML")))
                return len(lst_event_titles)
            return 0
        except Exception as error:
            raise RuntimeError("Fail to get prediction card titles on Live!") from error

    def find_seismic_event(self):
        """Method: find_seismic_event"""
        try:
            seismic_event_found = False
            lst_event_titles = self.return_object_list(ReadyLivePage.list_event_titles)
            assert len(lst_event_titles) > 0, "No seismic events found in Live!"
            for title in lst_event_titles:
                title_tmp = title.get_attribute("innerHTML")
                if "Earthquake" in title_tmp:
                    print("Live seismic event title: {}".format(title_tmp))
                    seismic_event_found = True
            return seismic_event_found
        except Exception as error:
            raise RuntimeError("Fail to find seismic event on Live!") from error

    def verify_no_seismic_event(self):
        """Method: verify_no_seismic_event"""
        try:
            lst_event_titles = self.return_object_list(ReadyLivePage.list_event_titles)
            assert (
                len(lst_event_titles) == 0
            ), "Expected No seismic events found in Live!"
            print("No seismic event found on Live page for Blue Sky!")
        except Exception as error:
            raise RuntimeError("Fail to verify no seismic event on Live!") from error

    def find_flood_event(self):
        """Method: find_flood_event"""
        try:
            flood_event_found = False
            lst_event_titles = self.return_object_list(ReadyLivePage.list_event_titles)
            assert len(lst_event_titles) > 0, "No flood events found in Live!"
            for title in lst_event_titles:
                title_tmp = title.get_attribute("innerHTML")
                if "Flood" in title_tmp:
                    print("Live flood event title: {}".format(title_tmp))
                    flood_event_found = True
            return flood_event_found
        except Exception as error:
            raise RuntimeError("Fail to find flood event on Live!") from error

    def verify_no_flood_event(self):
        """Method: verify_no_flood_event"""
        try:
            lst_event_titles = self.return_object_list(ReadyLivePage.list_event_titles)
            assert len(lst_event_titles) == 0, "Expected no flood event found in Live!"
            print("No flood event found on Live page for Blue Sky!")
        except Exception as error:
            raise RuntimeError("Fail to verify no flood event on Live!") from error

    def get_prediction_cards_total_impacted_people(self):
        """Method: get_prediction_cards_total_impacted_people"""
        try:
            assert (
                self.get_live_prediction_cards_titles() > 0
            ), "No prediction cards found in Live!"
            lst_total_impacted_people = self.return_object_list(
                ReadyLivePage.list_total_impacted_people
            )
            for tot_people in lst_total_impacted_people:
                print(
                    "Total impacted people: {}".format(
                        tot_people.get_attribute("innerHTML")
                    )
                )
        except Exception as error:
            raise RuntimeError("Fail to get total impacted people!") from error

    def get_prediction_cards_total_impacted_buildings(self):
        """Method: get_prediction_cards_total_impacted_buildings"""
        try:
            assert (
                self.get_live_prediction_cards_titles() > 0
            ), "No prediction cards found in Live!"
            lst_total_impacted_buildings = self.return_object_list(
                ReadyLivePage.list_total_impacted_buildings
            )
            for tot_buildings in lst_total_impacted_buildings:
                print(
                    "Total impacted buildings: {}".format(
                        tot_buildings.get_attribute("innerHTML")
                    )
                )
        except Exception as error:
            raise RuntimeError("Fail to get total impacted buildings!") from error

    def get_live_prediction_card_time_of_earthquake(self):
        """Method: get_live_prediction_card_time_of_earthquake"""
        try:
            lst_time_of_earthquakes = self.return_object_list(
                ReadyLivePage.list_earthquake_times
            )
            assert (
                len(lst_time_of_earthquakes) > 0
            ), "No prediction cards found in Live!"
            for earthquake_time in lst_time_of_earthquakes:
                print(
                    "Time of earthquake: {}".format(
                        earthquake_time.get_attribute("innerHTML")
                    )
                )
        except Exception as error:
            raise RuntimeError("Fail to get time of earthquake!") from error

    def get_live_prediction_card_magnitude(self):
        """Method: get_live_prediction_card_magnitude"""
        try:
            lst_magnitudes = self.return_object_list(
                ReadyLivePage.list_earthquake_magnitudes
            )
            assert len(lst_magnitudes) > 0, "No prediction cards found in Live!"
            for magnitude in lst_magnitudes:
                print(
                    "Magnitude of earthquake: {}".format(
                        magnitude.get_attribute("innerHTML")
                    )
                )
        except Exception as error:
            raise RuntimeError("Fail to get magnitude of earthquake!") from error

    def get_live_prediction_card_location(self):
        """Method: get_live_prediction_card_location"""
        try:
            lst_locations = self.return_object_list(
                ReadyLivePage.list_earthquake_locations
            )
            assert len(lst_locations) > 0, "No prediction cards found in Live!"
            for location in lst_locations:
                print(
                    "Location of earthquake: {}".format(
                        location.get_attribute("innerHTML")
                    )
                )
        except Exception as error:
            raise RuntimeError("Fail to get location of earthquake!") from error

    def get_live_prediction_card_epicenter(self):
        """Method: get_live_prediction_card_epicenter"""
        try:
            lst_epicenters = self.return_object_list(
                ReadyLivePage.list_earthquake_epicenters
            )
            assert len(lst_epicenters) > 0, "No prediction cards found in Live!"
            for epicenter in lst_epicenters:
                print(
                    "Epicenter of earthquake: {}".format(
                        epicenter.get_attribute("innerHTML")
                    )
                )
        except Exception as error:
            raise RuntimeError("Fail to get epicenter of earthquake!") from error

    def get_live_prediction_cards_depth(self):
        """ " Method: get_live_prediction_cards_depth"""
        try:
            lst_depths = self.return_object_list(ReadyLivePage.list_earthquake_depths)
            assert len(lst_depths) > 0, "No prediction cards found in Live!"
            for depth in lst_depths:
                print(
                    "Depth of earthquake: {}".format(depth.get_attribute("innerHTML"))
                )
        except Exception as error:
            raise RuntimeError("Fail to get depth of earthquake!") from error

    def click_flood_view_prediction_button(self):
        """ " Method: click_flood_view_prediction_button"""
        try:
            assert self.flood_event_found, "Found no flood predictions under Live!"
            self.click_element(ReadyLivePage.flood_view_prediction_btn)
        except Exception as error:
            raise RuntimeError("Fail to click Flood View Prediction button!") from error

    def click_seismic_view_prediction_button(self):
        """ " Method: click_seismic_view_prediction_button"""
        try:
            assert self.flood_event_found, "Found no flood predictions under Live!"
            self.click_element(ReadyLivePage.seismic_view_prediction_btn)
        except Exception as error:
            raise RuntimeError(
                "Fail to click Seismic View Prediction button!"
            ) from error

    def get_seismic_prediction_view_data(self):
        """Method: get_seismic_prediction_view_data"""
        try:
            seismic_header = self.get_text(ReadyLivePage.event_header_name)
            print("Got seismic header: {}".format(seismic_header))

            seismic_header_date = self.get_text(ReadyLivePage.event_header_updated)
            print("Got seismic posted date: {}".format(seismic_header_date))

            seismic_time_of_earthquake = self.get_inner_text(
                ReadyLivePage.time_of_earthquake
            )
            print(
                "Got seismic time of earthquake: {}".format(seismic_time_of_earthquake)
            )

            seismic_magnitude = self.get_inner_text(ReadyLivePage.magnitude)
            print("Got seismic magnitude: {}".format(seismic_magnitude))

            seismic_location = self.get_inner_text(ReadyLivePage.location)
            print("Got seismic location: {}".format(seismic_location))

            seismic_epicenter = self.get_inner_text(ReadyLivePage.epicenter)
            print("Got seismic epicenter: {}".format(seismic_epicenter))

            seismic_depth = self.get_inner_text(ReadyLivePage.depth)
            print("Got seismic depth: {}".format(seismic_depth))

            seismic_total_impact_buildings = self.get_inner_text(
                ReadyLivePage.total_impact_buildings
            )
            print(
                "Got total buildings impacted: {}".format(
                    seismic_total_impact_buildings
                )
            )

            seismic_total_impact_people = self.get_inner_text(
                ReadyLivePage.total_impact_people
            )
            print("Got total people impacted: {}".format(seismic_total_impact_people))
        except RuntimeError as error:
            self.generate_screenshot("seismic_prediction_data_error")
            raise RuntimeError(
                f"Fail to get seismic prediction view data due to: {error}"
            )

    def get_flood_prediction_view_data(self):
        """Method: get_flood_prediction_view_data"""
        try:
            assert self.flood_event_found, "Found no flood predictions under Live!"
            flood_header = self.get_text(ReadyLivePage.event_header_name)
            print("Got flood header: {}".format(flood_header))
            flood_header_date = self.get_text(ReadyLivePage.event_header_updated)
            print("Got flood posted date: {}".format(flood_header_date))
        except Exception as error:
            self.generate_screenshot("flood_prediction_data_error")
            raise RuntimeError("Fail to get flood prediction view data!") from error

    def get_library_flood_prediction_view_data(self):
        """Method: get_library_flood_prediction_view_data"""
        try:
            prediction_view_data = {}
            prediction_view_data["alert_panel_title"] = self.get_text(
                ReadyLivePage.alert_panel_title
            )
            prediction_view_data["flood_header"] = self.get_text(
                ReadyLivePage.event_header_name
            )
            prediction_view_data["flood_header_date"] = self.get_text(
                ReadyLivePage.event_header_updated
            )
            prediction_view_data["inundated_area"] = self.get_text(
                ReadyLivePage.inundated_area
            )
            prediction_view_data["total_buildings_impacted"] = self.get_text(
                ReadyLivePage.total_impact_buildings1
            )
            prediction_view_data["total_people_impacted"] = self.get_text(
                ReadyLivePage.total_impact_people1
            )
            prediction_view_data["flood_depth_2in"] = self.get_text(
                ReadyLivePage.flood_depth_2_to_6_in
            )
            prediction_view_data["flood_depth_6in"] = self.get_text(
                ReadyLivePage.flood_depth_6in_to_1ft
            )
            prediction_view_data["flood_depth_1ft"] = self.get_text(
                ReadyLivePage.flood_depth_1_to_2ft
            )
            prediction_view_data["flood_depth_2ft"] = self.get_text(
                ReadyLivePage.flood_depth_2_to_3ft
            )
            prediction_view_data["flood_depth_3ft"] = self.get_text(
                ReadyLivePage.flood_depth_3_to_4ft
            )
            prediction_view_data["flood_depth_4ft"] = self.get_text(
                ReadyLivePage.flood_depth_4_to_5ft
            )
            prediction_view_data["flood_depth_5ft"] = self.get_text(
                ReadyLivePage.flood_depth_5_to_6ft
            )
            prediction_view_data["flood_depth_6ft"] = self.get_text(
                ReadyLivePage.flood_depth_greater_6ft
            )
            print(
                f"Alert Predicted Overflow Points: {prediction_view_data['alert_panel_title']}"
            )
            print(f"Got flood header: {prediction_view_data['flood_header']}")
            print(f"Got flood posted date: {prediction_view_data['flood_header_date']}")
            print(f"Got inundated area: {prediction_view_data['inundated_area']}")
            print(
                f"Got total buildings impacted: {prediction_view_data['total_buildings_impacted']}"
            )
            print(
                f"Got total people impacted: {prediction_view_data['total_people_impacted']}"
            )
            print(f"Got flood depth at 2in: {prediction_view_data['flood_depth_2in']}")
            print(f"Got flood depth at 6in: {prediction_view_data['flood_depth_6in']}")
            print(f"Got flood depth at 1ft: {prediction_view_data['flood_depth_1ft']}")
            print(f"Got flood depth at 2ft: {prediction_view_data['flood_depth_2ft']}")
            print(f"Got flood depth at 3ft: {prediction_view_data['flood_depth_3ft']}")
            print(f"Got flood depth at 4ft: {prediction_view_data['flood_depth_4ft']}")
            print(f"Got flood depth at 5ft: {prediction_view_data['flood_depth_5ft']}")
            print(
                f"Got flood depth at greater than 6ft: {prediction_view_data['flood_depth_6ft']}"
            )
        except Exception as error:
            self.generate_screenshot("flood_prediction_data_error")
            raise RuntimeError("Fail to get flood prediction view data!") from error

    def get_river_gauge_names(self, geo):
        """Method: get_river_gauge_names"""
        try:
            lstactualrivergauges = []
            lst_kcexpected = ["代継橋", "城南", "御船", "大六橋"]
            lst_kawasakiexpected = ["寺家橋", "石原"]
            lst_koriyamaexpected = ["須賀川", "阿久津"]
            lst_naganoexpected = ["小市", "立ヶ花"]
            lst_okayamaexpected = ["下牧", "御休"]
            lst_okazakiexpected = ["木戸", "岩津"]
            lstrivergaugeobjects = self.return_object_list(
                ReadyLivePage.river_gauge_names
            )
            for river_gauge_name in lstrivergaugeobjects:
                rgname = river_gauge_name.text
                print(f"Got River Gauge Name: {rgname}")
                lstactualrivergauges.append(rgname)
            if geo == "kc":
                assert lst_kcexpected == lstactualrivergauges
            if geo == "kawasaki":
                assert lst_kawasakiexpected == lstactualrivergauges
            if geo == "koriyama":
                assert lst_koriyamaexpected == lstactualrivergauges
            if geo == "nagano":
                assert lst_naganoexpected == lstactualrivergauges
            if geo == "okayama":
                assert lst_okayamaexpected == lstactualrivergauges
            if geo == "okazaki":
                assert lst_okazakiexpected == lstactualrivergauges
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get river gauge names!") from error

    def verify_river_gauge_graphs(self, geo):
        """Method: verify_river_gauge_graphs
        Use this method if river gauge button is present
        """
        try:
            self.click_element(ReadyLivePage.river_gauges_btn)
            self.element_present(ReadyLivePage.river_gauges_header)
            lst_river_gauge_graphs = self.return_object_list(
                ReadyLivePage.river_gauge_chart
            )
            actual_total_river_gauge_graphs = len(lst_river_gauge_graphs)
            print(
                f"Found for: {geo}, total river gauge graphs: {actual_total_river_gauge_graphs}"
            )
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to verify river gauge graphs!") from error

    def verify_river_gauges(self, geo):
        """Method: verify_river_gauges
        Use this method if river gauge button is present
        """
        try:
            lst_river_gauge_names = []
            self.click_element(ReadyLivePage.river_gauges_btn)
            self.element_present(ReadyLivePage.river_gauges_header)
            lst_river_gauges = self.return_object_list(ReadyLivePage.river_gauge_name)
            for item in lst_river_gauges:
                print(item.text)
                lst_river_gauge_names.append(item.text)
            actual_total_river_gauges = len(lst_river_gauge_names)
            print(f"Found for: {geo}, total river gauges: {actual_total_river_gauges}")
            if geo == "kc":
                expected_river_gauge_names = ["代継橋", "城南", "御船", "大六橋"]
                assert (
                    actual_total_river_gauges == 4
                ), f"Wrong number of river gauges found for {geo}!"
                assert (
                    lst_river_gauge_names == expected_river_gauge_names
                ), f"Wrong river gauge names for {geo}!"
            if geo == "kawasaki":
                expected_river_gauge_names = ["寺家橋", "石原"]
                assert (
                    actual_total_river_gauges == 2
                ), f"Wrong number of river gauges found for {geo}!"
                assert (
                    lst_river_gauge_names == expected_river_gauge_names
                ), f"Wrong river gauge names for {geo}!"
            if geo == "koriyama":
                expected_river_gauge_names = ["阿久津", "須賀川"]
                assert (
                    actual_total_river_gauges == 2
                ), f"Wrong number of river gauges found for {geo}!"
                assert (
                    lst_river_gauge_names == expected_river_gauge_names
                ), f"Wrong river gauge names for {geo}!"
            if geo == "nagano":
                expected_river_gauge_names = ["小市", "立ヶ花"]
                assert (
                    actual_total_river_gauges == 2
                ), f"Wrong number of river gauges found for {geo}!"
                assert (
                    lst_river_gauge_names == expected_river_gauge_names
                ), f"Wrong river gauge names for {geo}!"
            if geo == "okayama":
                expected_river_gauge_names = ["御休", "下牧"]
                assert (
                    actual_total_river_gauges == 2
                ), f"Wrong number of river gauges found for {geo}!"
                assert (
                    lst_river_gauge_names == expected_river_gauge_names
                ), f"Wrong river gauge names for {geo}!"
            if geo == "okazaki":
                expected_river_gauge_names = ["木戸", "岩津"]
                assert (
                    actual_total_river_gauges == 2
                ), f"Wrong number of river gauges found for {geo}!"
                assert (
                    lst_river_gauge_names == expected_river_gauge_names
                ), f"Wrong river gauge names for {geo}!"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to verify river gauges!") from error

    def get_gauge_addresses(self):
        """Method: get_gauge_addresses"""
        try:
            lst_gauge_addresses_text = []
            if self.element_present(ReadyLivePage.river_gauges_header):
                lst_gauge_addresses = self.return_object_list(
                    ReadyLivePage.river_gauge_address
                )
                assert len(lst_gauge_addresses) > 0, "Found no gauge addresses!"
                for item in lst_gauge_addresses:
                    print(item.text)
                    lst_gauge_addresses_text.append(item.text)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get gauge addresses!") from error

    def get_river_systems(self):
        """Method: get_river_systems"""
        try:
            lst_river_system_text = []
            if self.element_present(ReadyLivePage.river_gauges_header):
                lst_river_system = self.return_object_list(ReadyLivePage.river_system)
                assert len(lst_river_system) > 0, "Found no river systems!"
                for item in lst_river_system:
                    print(item.text)
                    lst_river_system_text.append(item.text)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get river systems!") from error

    def get_river_names(self):
        """Method: get_river_names"""
        try:
            lst_river_names_text = []
            if self.element_present(ReadyLivePage.river_gauges_header):
                lst_river_names = self.return_object_list(
                    ReadyLivePage.river_gauge_names
                )
                assert len(lst_river_names) > 0, "Found no river names!"
                for item in lst_river_names:
                    print(item.text)
                    lst_river_names_text.append(item.text)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get river names!") from error

    def get_river_threshold_list(self):
        """Method: get_river_threshold_list"""
        try:
            lst_river_threshold_list_text = []
            if self.element_present(ReadyLivePage.river_gauges_header):
                lst_river_threshold_list = self.return_object_list(
                    ReadyLivePage.river_threshold_reached_list
                )
                if len(lst_river_threshold_list) > 0:
                    for item in lst_river_threshold_list:
                        if len(item.text) > 0:
                            print(item.text)
                            lst_river_threshold_list_text.append(item.text)
                if len(lst_river_threshold_list_text) == 0:
                    print("Empty threshold list!")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get river threshold list!") from error

    def get_river_threshold_legend_text(self):
        """Method: get_river_threshold_legend_text"""
        try:
            lst_river_threshold_legend_text = []
            if self.element_present(ReadyLivePage.river_gauges_header):
                lst_river_threshold_legend = self.return_object_list(
                    ReadyLivePage.river_threshold_legend_text
                )
                if len(lst_river_threshold_legend) > 0:
                    for item in lst_river_threshold_legend:
                        print(item.text)
                        lst_river_threshold_legend_text.append(item.text)
                else:
                    print("Found no river threshold legend text!")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to get river threshold legend!") from error

    def get_posted(self):
        """Method: get_posted"""
        try:
            posted_datetime = self.get_text(ReadyLivePage.posted)
            print("Got actual Posted: {}".format(posted_datetime))
            return posted_datetime
        except Exception as error:
            raise RuntimeError("Fail to get posted from River Gauge!") from error

    def get_weather_forecast_time(self):
        """Method: get_weather_forecast_time"""
        try:
            weather_forecast_time = self.get_text(ReadyLivePage.weather_forecast_time)
            print("Got actual Weather forecast time: {}".format(weather_forecast_time))
            return weather_forecast_time
        except Exception as error:
            raise RuntimeError(
                "Fail to get Weather forecast time from River Gauge!"
            ) from error

    def get_max_1hr_rainfall(self):
        """Method: get_max_1hr_rainfall"""
        try:
            max_1hr_rainfall = self.get_text(ReadyLivePage.max_1hr_rainfall)
            print("Got actual Max 1hr rainfall: {}".format(max_1hr_rainfall))
            return max_1hr_rainfall
        except Exception as error:
            raise RuntimeError(
                "Fail to get Max 1-hr rainfall from River Gauge!"
            ) from error

    def get_max_24hr_rainfall(self):
        """Method: get_max_24hr_rainfall"""
        try:
            max_24hr_rainfall = self.get_text(ReadyLivePage.max_24hr_rainfall)
            print("Got actual Max 24hr rainfall: {}".format(max_24hr_rainfall))
            return max_24hr_rainfall
        except Exception as error:
            raise RuntimeError(
                "Fail to get Max 24-hr rainfall from River Gauge!"
            ) from error

    def verify_view_mlit_links(self, geo):
        """Method: verify_view_mlit_limks"""
        try:
            lstviewmlit = self.return_object_list(ReadyLivePage.view_mlit_links)
            totalviewmlit = len(lstviewmlit)
            print(f"Actual View MLIT links: {totalviewmlit}")
            if geo == "kc":
                assert totalviewmlit == 4, "Wrong number of View MLIT links!"
            if geo in ["kawasaki", "koriyama", "nagano", "okayama", "okazaki"]:
                assert totalviewmlit == 2, "Wrong number of View MLIT links!"
        except Exception as error:
            raise RuntimeError(
                "Fail to verify View MLIT links for geo: {geo}!"
            ) from error

    def show_no_live_river_gauge_predictions(self):
        """Method: show_no_live_river_gauge_predictions"""
        try:
            expect = "There are no river gauges for your region."
            actual = self.get_text(
                ReadyLivePage.no_live_river_gauge_predictions_available
            )
            print(f"Actual text: {actual}")
            assert (
                expect == actual
            ), "Wrong message displayed for no Live river gauge predictions available!"
        except Exception as error:
            raise RuntimeError(
                "Fail to get no Live river gauge predictions!"
            ) from error

    def verify_graph_units(self):
        """Method: verify_graph_units"""
        try:
            actual_units = self.get_text(ReadyLivePage.units_meters)
            print(f"Actual units: {actual_units[-1]}")
            assert actual_units[-1] == "m", "Expected units in meters!"
        except Exception as error:
            raise RuntimeError("Fail to get river gauge graph units!") from error

    def switch_locale_verify_units(self):
        """Method: switch_locale_verify_units"""
        try:
            locale = {
                "staging_en": "https://auth.staging.onec.co/auth/realms/oneconcern/login-actions/authenticate?kc_locale=en",
                "staging_ja": "https://auth.staging.onec.co/auth/realms/oneconcern/login-actions/authenticate?kc_locale=ja",
                "prod_en": "https://auth.oneconcern.com/auth/realms/oneconcern/login-actions/authenticate?kc_locale=en",
                "prod_ja": "https://auth.oneconcern.com/auth/realms/oneconcern/login-actions/authenticate?kc_locale=ja",
            }

            home = {
                "staging": "https://app.staging.onec.co/#/home",
                "prod": "https://app.oneconcern.com/#/home",
            }

            print(f"Got URL: {self.url}")
            if "staging" in self.url:
                self.verify_graph_units()
                print("Switching to JP locale for staging to verify units...")
                self.driver.get(locale["staging_ja"])
                self.driver.get(home["staging"])
                self.element_present(ReadyLivePage.units_meters)
                self.verify_graph_units()
                # Return to EN locale for staging
                self.driver.get(locale["staging_en"])
                self.driver.get(home["staging"])
            else:
                self.verify_graph_units()
                print("Switching to JP locale for production to verify units...")
                self.driver.get(locale["prod_ja"])
                self.driver.get(home["prod"])
                self.element_present(ReadyLivePage.units_meters)
                self.verify_graph_units()
                # Return to EN locale for production
                self.driver.get(locale["prod_en"])
                self.driver.get(home["prod"])
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to switch locale and verify units!") from error

    def get_graph_start_time(self):
        """Method: get_graph_start_time"""
        try:
            actual_graph_start_time = self.get_text(ReadyLivePage.graph_start_time)
            print(f"Actual graph start time: {actual_graph_start_time}")
            return actual_graph_start_time
        except Exception as error:
            raise RuntimeError("Fail to get river gauge graph start time!") from error

    def get_graph_end_time(self):
        """Method: get_graph_end_time"""
        try:
            actual_graph_end_time = self.get_text(ReadyLivePage.graph_end_time)
            print(f"Actual graph end time: {actual_graph_end_time}")
            return actual_graph_end_time
        except Exception as error:
            raise RuntimeError("Fail to get river gauge graph stop time!") from error

    def verify_threshold_chart_legend(self, geo):
        """Method: verify_threshold_chart_legend"""
        try:
            lstThresholdChartLegend = self.return_object_list(
                ReadyLivePage.threshold_chart_legend
            )
            totThresholdChartLegends = len(lstThresholdChartLegend)
            print(f"Actual Threshold Chart Legends: {totThresholdChartLegends}")
            if geo == "kc":
                assert totThresholdChartLegends == 4, "Missing Threshold Chart Legend!"
            if geo in ["kawasaki", "koriyama", "nagano", "okayama", "okazaki"]:
                assert totThresholdChartLegends == 2, "Missing Threshold Chart Legend!"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError(
                "Fail to verify Threshold Chart Legends for geo: {geo}!"
            ) from error

    def get_no_stats_message(self):
        """Method: get_no_stats_message"""
        try:
            lstNoStatsMessages = self.return_object_list(ReadyLivePage.no_stats_message)
            totalNoStatsMessages = len(lstNoStatsMessages)
            print(f"Found total 'No Stats Messages': {totalNoStatsMessages}")
            if totalNoStatsMessages > 0:
                print(
                    "Got No Stats Message:"
                    + self.get_text(ReadyLivePage.no_stats_message)
                )
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError(
                "Fail to verify 'No Stats Messages' in River Gauge Graph!"
            ) from error

    def get_threshold_reached_list(self):
        """Method: get_threshold_reached_list"""
        try:
            lstThresholdReachedList = self.return_object_list(
                ReadyLivePage.threshold_reached_list
            )
            totThresholdReachedList = len(lstThresholdReachedList)
            print(f"Found total 'Threshold Reached List': {totThresholdReachedList}")
            lstLevel2ThresholdMessages = self.return_object_list(
                ReadyLivePage.threshold_level_2_text
            )
            if len(lstLevel2ThresholdMessages) > 0:
                lvl2_message = self.get_inner_text(ReadyLivePage.threshold_level_2_text)
                print(f"Got Level 2 threshold message: {lvl2_message}")
            else:
                print("Found no level 2 threshold levels!")
            lstLevel3ThresholdMessages = self.return_object_list(
                ReadyLivePage.threshold_level_3_text
            )
            if len(lstLevel3ThresholdMessages) > 0:
                lvl3_message = self.get_inner_text(ReadyLivePage.threshold_level_3_text)
                print(f"Got Level 3 threshold message: {lvl3_message}")
            else:
                print("Found no level 3 threshold levels!")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError(
                "Fail to verify 'No Stats Messages' in River Gauge Graph!"
            ) from error

    def click_play(self):
        """Method: click_play"""
        try:
            self.pause(5)
            self.generate_screenshot(inspect.stack()[0][3] + "_play_before")
            self.click_element(ReadyLivePage.play_button, 5)
            self.generate_screenshot(inspect.stack()[0][3] + "_play_after")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to click Play button!") from error
