""" ReadyLibraryPage.py """
import inspect
from ReadyLivePage import ReadyLivePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ReadyLibraryPage(ReadyLivePage):
    """ Class: ReadyLibraryPage """

    first_event = 'a:nth-child(1) > div > div'
    seismic_library_card_list = 'div[data-test-id="library-card-list"] a[data-test-hazard-type=["Seismic"]'
    flood_library_card_list = 'div[data-test-id="library-card-list"] a[data-test-hazard-type=["Flood"]'
    seismic_simulation_btn = 'button[data-test-id="RequestSimulationButton"]'
    first_event_header_name = 'span[data-test-id="EventHeader-name"]'
    first_event_header_updated = 'span[data-test-id="EventHeader-updated"]'
    first_time_of_earthquake = '[data-test-id="startTime"] > [data-test-id="value"]'
    first_magnitude = '[data-test-id="magnitude"] > [data-test-id="value"]'
    first_location = '[data-test-id="location"] > [data-test-id="value"]'
    first_epicenter = '[data-test-id="epicenter"] > [data-test-id="value"]'
    first_depth = '[data-test-id="earthquakeDepth"] > [data-test-id="value"]'
    first_total_impact_buildings = '[data-test-id="StatsTable-impactedBuildings"] > [data-test-id2="StatsRow-total"] > [data-test-id="value"]'
    first_total_impact_people = '[data-test-id="StatsTable-impactedPeople"] > [data-test-id2="StatsRow-total"] > [data-test-id="value"]'
    prediction_card_titles = '[data-test-id="event-title-text"]'
    library_urls = 'div[data-test-id="library-card-list"] a'
    library_card_types = '[data-test-id="eventType"]'
    library_total_impacted_people = '[data-test-id="Stat-numPeople"]'
    library_total_impacted_buildings = '[data-test-id="Stat-numBuildings"]'
    library_time_of_earthquake = '[data-test-id="startTime"]'
    library_magnitude = '[data-test-id="magnitude"]'
    library_location = '[data-test-id="location"]'
    library_epicenter = '[data-test-id="epicenter"]'
    library_depth = '[data-test-id="earthquakeDepth"]'
    great_tohuku_impact_people_nmbr = (By.XPATH, '//*[contains(@title,"great-tohuku-auto-")]/../../../..//span[contains(@data-test-id, "Stat-numPeople")]')
    impact_people_nmbr_by_geo = (By.XPATH, f'//*[contains(@title,"{None}")]/../../../..//span[contains(@data-test-id, "Stat-numPeople")]')
    library_river_gauge_tab = '[data-test-id="SidePanelNav-RiverGauges"]'
    flood_prediction_cards = '[data-test-hazard-type="Flood"]'
    river_gauge_not_available = '[data-test-id="GaugeDataUnavailable"]'

    def click_first_historical_seismic_event(self):
        """ Method: find_first_historical_seismic_event """
        try:
            lsteventtitles = self.return_object_list(ReadyLibraryPage.prediction_card_titles)
            lstcardtypes = self.return_object_list(ReadyLibraryPage.library_card_types)
            assert len(lstcardtypes) > 0, "Found no predication cards under Library!"
            #Get all card types
            lstallcardtypes = []
            for cardtype in lstcardtypes:
                cardtype_label = cardtype.text
                lstallcardtypes.append(cardtype_label)
            #Get all prediction card titles
            lstallpredictioncardtitles = []
            for event in lsteventtitles:
                event_label = event.text
                lstallpredictioncardtitles.append(event_label)
            #Create a list of tuples
            merged_list = tuple(zip(lstallpredictioncardtitles, lstallcardtypes))
            #Find the first Historical Seismic event under Library
            iCount = 1
            for cardtitle, cardtype in merged_list:
                print(f"Got card title: {cardtitle} with card type: {cardtype} at card number: {iCount}")
                if "Earthquake" in cardtitle and cardtype == "Historical":
                    print(f"Found first historical seismic event: {cardtitle}")
                    seismic_element = "div[data-test-id=\"library-card-list\"] a:nth-child(" + str(iCount) + ")"
                    self.driver.find_element(By.CSS_SELECTOR, seismic_element).click()
                    break
                iCount += 1
        except Exception as error:
            self.generate_screenshot("click_first_historical_seismic_event_error")
            raise RuntimeError("Fail to find first historical seismic event!") from error

    def choose_first_historical_flood_event(self):
        """ Method: choose_first_historical_flood_event """
        try:
            lstfloodpc = self.return_object_list(ReadyLibraryPage.flood_prediction_cards)
            print(f"Found total Library flood prediction cards:{len(lstfloodpc)}")
            assert len(lstfloodpc) > 0, "Found no flood predication cards under Library!"
            for item in lstfloodpc:
                flood_url = item.get_attribute("href")
                print(f"Use flood URL: {flood_url}")
                self.driver.get(flood_url)
                break
            self.element_present(ReadyLibraryPage.first_event_header_name)
        except Exception as error:
            self.generate_screenshot("click_first_historical_flood_event_error")
            raise RuntimeError("Fail to find first historical flood event!") from error

    def click_first_prediction_card(self):
        """ Method: click_first_prediction_card """
        try:
            lst_event_titles = self.return_object_list(ReadyLibraryPage.prediction_card_titles)
            assert len(lst_event_titles) > 0, "No Library events found!"
            self.click_element(ReadyLibraryPage.first_event)
        except Exception as error:
            raise RuntimeError("Fail to click first prediction card!") from error

    def get_all_library_urls(self):
        """ Method: get_all_library_urls """
        try:
            lst_event_urls = self.return_object_list(ReadyLibraryPage.library_urls)
            print("Total Library events found:", len(lst_event_urls))
            assert len(lst_event_urls) > 0, "No Library events found!"
            for url in lst_event_urls:
                str_url = str(url.get_attribute("href"))
                print("Library event URL: " + str_url)
        except Exception as error:
            raise RuntimeError("Fail to get all predictions!") from error

    def get_first_prediction_view(self):
        """ Method: show_first_prediction_view """
        try:
            seismic_header = self.get_text(ReadyLibraryPage.first_event_header_name)
            print("Got seismic header: {}".format(seismic_header))

            seismic_header_date = self.get_text(ReadyLibraryPage.first_event_header_updated)
            print("Got seismic posted date: {}".format(seismic_header_date))

            seismic_time_of_earthquake = self.get_inner_text(ReadyLibraryPage.first_time_of_earthquake)
            print("Got seismic time of earthquake: {}".format(seismic_time_of_earthquake))

            seismic_magnitude = self.get_inner_text(ReadyLibraryPage.first_magnitude)
            print("Got seismic magnitude: {}".format(seismic_magnitude))

            seismic_location = self.get_inner_text(ReadyLibraryPage.first_location)
            print("Got seismic location: {}".format(seismic_location))

            seismic_epicenter = self.get_inner_text(ReadyLibraryPage.first_epicenter)
            print("Got seismic epicenter: {}".format(seismic_epicenter))

            seismic_depth = self.get_inner_text(ReadyLibraryPage.first_depth)
            print("Got seismic depth: {}".format(seismic_depth))

            seismic_total_impact_buildings = self.get_inner_text(ReadyLibraryPage.first_total_impact_buildings)
            print("Got total buildings impacted: {}".format(seismic_total_impact_buildings))

            seismic_total_impact_people = self.get_inner_text(ReadyLibraryPage.first_total_impact_people)
            print("Got total people impacted: {}".format(seismic_total_impact_people))
        except Exception as error:
            self.generate_screenshot("first_seismic_prediction_data_error")
            raise RuntimeError("Fail to get seismic prediction view data for first prediction card!") from error

    def verify_seismic_simulation(self):
        """ Method: verify_seismic_simulation """
        try:
            assert len(self.return_object_list(ReadyLibraryPage.seismic_simulation_btn)) == 0, "Found Seismic Simulation button!"
            print("Detected no Seismic Simulation button!")
        except Exception as error:
            self.generate_screenshot("seismic_simulation_button_error")
            raise RuntimeError("Fail in verifying Seismic Simulation button!") from error

    def verify_library_events(self):
        """ Method: verify_library_events """
        try:
            lst_event_titles_library = self.return_object_list(ReadyLibraryPage.prediction_card_titles)
            assert len(lst_event_titles_library) > 0, "No Library event found!"
            tot_flood = 0
            tot_seismic = 0
            for title in lst_event_titles_library:
                event_title = title.get_attribute("innerHTML")
                print("Prediction Card Title: {}".format(event_title))
                if "Flood" in event_title:
                    tot_flood += 1
                if "Earthquake" in event_title:
                    tot_seismic += 1
        except Exception as error:
            raise RuntimeError("Fail to get all Library prediction card titles!") from error

    def get_all_prediction_cards_titles(self):
        """ Method: get_all_prediction_cards_titles """
        try:
            lst_event_titles_library = self.return_object_list(ReadyLibraryPage.prediction_card_titles)
            assert len(lst_event_titles_library) > 0, "No Library events found!"
            for title in lst_event_titles_library:
                print("Library Prediction Card Title: {}".format(title.get_attribute("innerHTML")))
        except Exception as error:
            raise RuntimeError("Fail to get all Library prediction card titles!") from error

    def get_all_prediction_cards_types(self):
        """ Method: get_all_prediction_cards_types """
        try:
            lst_event_types_library = self.return_object_list(ReadyLibraryPage.library_card_types)
            assert len(lst_event_types_library) > 0, "No Library events found!"
            for event_type in lst_event_types_library:
                print("Library Card Type: {}".format(event_type.get_attribute("innerHTML")))
        except Exception as error:
            raise RuntimeError("Fail to get all Library prediction card types!") from error

    def get_all_prediction_cards_total_impacted_people(self):
        """ Method: get_all_prediction_cards_total_impacted_people """
        try:
            lst_total_impacted_people_library = self.return_object_list(ReadyLibraryPage.library_total_impacted_people)
            assert len(lst_total_impacted_people_library) > 0, "No Library events found!"
            for tot_people in lst_total_impacted_people_library:
                print("Total Library impacted people: {}".format(tot_people.get_attribute("innerHTML")))
        except Exception as error:
            raise RuntimeError("Fail to get Library total impacted people!") from error

    def get_all_prediction_cards_total_impacted_buildings(self):
        """ Method: get_all_prediction_cards_total_impacted_buildings """
        try:
            lst_total_impacted_buildings_library = self.return_object_list(ReadyLibraryPage.library_total_impacted_buildings)
            assert len(lst_total_impacted_buildings_library) > 0, "No Library events found!"
            for tot_buildings in lst_total_impacted_buildings_library:
                print("Total Library impacted buildings: {}".format(tot_buildings.get_attribute("innerHTML")))
        except Exception as error:
            raise RuntimeError("Fail to get Library total impacted buildings!") from error

    def get_all_prediction_cards_time_of_earthquake(self):
        """ Method: get_all_prediction_cards_time_of_earthquake """
        try:
            lst_time_of_earthquakes_library = self.return_object_list(ReadyLibraryPage.library_time_of_earthquake)
            assert len(lst_time_of_earthquakes_library) > 0, "No Library events found!"
            for earthquake_time in lst_time_of_earthquakes_library:
                print("Library Time of earthquake: {}".format(earthquake_time.get_attribute("innerHTML")))
        except Exception as error:
            raise RuntimeError("Fail to get time of earthquake!") from error

    def get_all_prediction_cards_magnitude(self):
        """ Method: get_all_prediction_cards_magnitude """
        try:
            lst_magnitudes_library = self.return_object_list(ReadyLibraryPage.library_magnitude)
            assert len(lst_magnitudes_library) > 0, "No Library events found!"
            for magnitude in lst_magnitudes_library:
                print("Library Magnitude of earthquake: {}".format(magnitude.get_attribute("innerHTML")))
        except Exception as error:
            raise RuntimeError("Fail to get Library magnitude of earthquake!") from error

    def get_all_prediction_cards_location(self):
        """ Method: get_all_prediction_cards_location """
        try:
            lst_locations_library = self.return_object_list(ReadyLibraryPage.library_location)
            assert len(lst_locations_library) > 0, "No Library events found!"
            for location in lst_locations_library:
                print("Library Location of earthquake: {}".format(location.get_attribute("innerHTML")))
        except Exception as error:
            raise RuntimeError("Fail to get Library location of earthquake!") from error

    def get_all_prediction_cards_epicenter(self):
        """ Method: get_all_prediction_cards_epicenter """
        try:
            lst_epicenters_library = self.return_object_list(ReadyLibraryPage.library_epicenter)
            assert len(lst_epicenters_library) > 0, "No Library events found!"
            for epicenter in lst_epicenters_library:
                print("Library Epicenter of earthquake: {}".format(epicenter.get_attribute("innerHTML")))
        except Exception as error:
            raise RuntimeError("Fail to get Library epicenter of earthquake!") from error

    def get_all_prediction_cards_depth(self):
        """ Method: get_all_prediction_cards_depth """
        try:
            lst_depths_library = self.return_object_list(ReadyLibraryPage.library_depth)
            assert len(lst_depths_library) > 0, "No Library events found!"
            for depth in lst_depths_library:
                print("Library Depth of earthquake: {}".format(depth.get_attribute("innerHTML")))
        except Exception as error:
            raise RuntimeError("Fail to get Library depth of earthquake!") from error

    def impacted_people_shouldnt_appear(self,number):
        """ Method: impacted_people_from_kawasaki_shouldnt_appear """
        try:
            impact_people = self.driver.find_element(*ReadyLibraryPage.great_tohuku_impact_people_nmbr).text
            chiba_impact = impact_people.replace(',','')
            should_not_have = number
            if int(chiba_impact) != int(should_not_have):
                pass
            else:
                raise Exception("The impacted number is not correct")
        except Exception as e:
            raise Exception("The impacted number is not correct due to: " + str(e))


    def impacted_geo_people_should_be(self,geo,impacted):
        """ Method: impacted_geo_people_should_be """
        try:
            impact_people = self.driver.find_element(By.XPATH, f'//*[contains(@title,"{geo}")]/../../../..//span[contains(@data-test-id, "Stat-numPeople")]').text
            impact_number = impact_people.replace(',','')
            should_have = impacted
            if int(impact_number) == int(should_have):
                pass
            else:
                raise Exception(f"The impacted people number for {geo} is not correct")
        except Exception as error:
            raise RuntimeError(f"The impacted >{impact_number}< people number from {geo} is not correct!") from error

    def impacted_geo_building_should_be(self,geo,impacted):
        """ Method: impacted_geo_building_should_be """
        try:
            if geo == "great-tohuku-auto-":
                impact_building = self.driver.find_element(By.XPATH, f'(//*[contains(text(),"{geo}")]/../../../following-sibling::div[1]/div/div[3]/span)[1]').text
                # TRY:
                # impact_building = self.driver.find_element(By.XPATH, f'//*[contains(@title,"{geo}")]/../../../..//span[contains(@data-test-id, "Stat-numBuildings")]').text
            elif geo =="kawasaki-auto-":
                impact_building = self.driver.find_element(By.XPATH, f'(//*[contains(text(),"{geo}")]/../../../following-sibling::div[1]/div/div[3]/span)[2]').text
                # TRY:
                # impact_building = self.driver.find_element(By.XPATH, f'//*[contains(@title,"{geo}")]/../../../..//span[contains(@data-test-id, "Stat-numBuildings")]').text
            else:
                impact_building = self.driver.find_element(By.XPATH, f'(//*[contains(text(),"{geo}")]/../../../following-sibling::div[1]/div/div[3]/span)[1]').text
                # TRY:
                # time.sleep(60)
                # impact_building = self.driver.find_element(By.XPATH, f'//*[contains(@title,"{geo}")]/../../../..//span[contains(@data-test-id, "Stat-numBuildings")]').text

            impact_number = impact_building.replace(',','')
            should_have = impacted
            if int(impact_number) == int(should_have):
                pass
            else:
                raise Exception(f"The impacted building number for {geo} is not correct")
        except Exception as error:
            raise RuntimeError(f"The impacted >{impact_number}< building number from {geo} is not correct!") from error

    def click_card_with_title(self,title):
        """ Method: click_card_with_title """
        # self.element_present('[data-test-id="Stat-numBuildings"]')
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH, f'(//*[contains(text(),"{title}")]/../../../following-sibling::div[1]/div/div[contains(@class, "u-marginbottom--20")]/span)[1]')).perform()
        try:
            self.driver.find_element(By.XPATH, f'(//*[contains(text(),"{title}")]/../../../following-sibling::div[1]/div/div[contains(@class, "u-marginbottom--20")]/span)[1]').click()
        except Exception as error:
            raise RuntimeError("Couldn't click the card!") from error

    def verify_river_gauge_tab(self):
        """ Method: verify_river_gauge_tab """
        try:
            if self.element_present(ReadyLibraryPage.library_river_gauge_tab):
                print("PASS: Found river gauge tab!")
            else:
                raise Exception("FAIL: Found no river gauge tab as expected!")
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to verify river gauge tab is present!") from error

    def verify_no_river_gauge_station(self):
        """ Method: verify_no_river_gauge_station """
        try:
            self.click_element(ReadyLibraryPage.river_gauges_btn)
            message = self.get_text(ReadyLibraryPage.river_gauge_not_available)
            print(f"Got this message: {message}")
            assert message == "Data for river gauge stations is not available at this time.", "Expect message with no river gauge station available!"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Failed to verify text for no river gauge station is available!!") from error

    def verify_no_simulation_events(self):
        """ Method: verify_no_simulation_events """
        try:
            lstcardtypes = self.return_object_list(ReadyLibraryPage.library_card_types)
            print(f"Total card types: {len(lstcardtypes)}")
            assert len(lstcardtypes) > 0, "Found no predication cards under Library!"
            #Checking for Simulation events under Library
            lstSimulationEvents = []
            i = 1
            for cardtype in lstcardtypes:
                cardtype_label = cardtype.text
                print(f"Got event type for card #: {i}: {cardtype_label}")
                if cardtype_label == "Simulation":
                    lstSimulationEvents.append(cardtype_label)
                i += 1
            assert len(lstSimulationEvents) == 0, "Found Simulation events!"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Detected a 'Simulation' event under Library!") from error
