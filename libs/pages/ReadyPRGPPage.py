""" ReadyPRGPPage.py """
import inspect
from ReadyLivePage import ReadyLivePage


class ReadyPRGPPage(ReadyLivePage):
    """ Class: ReadyPRGPPage """

    no_past_river_gauge_predictions_available = '[data-test-id="EmptyLibraryView"] > span'

    def get_max_past_river_gauge_predictions(self):
        """ Method: get_max_past_river_gauge_predictions """
        try:
            lst_links = self.return_object_list(ReadyLivePage.past_river_gauge_blocks)
            print("Got total number of past river gauge predictions: {}".format(len(lst_links)))
            assert len(lst_links) == 8, "Expected 8 Past River Gauge Predictions for viewing!"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get maximum past river gauge predictions!") from error

    def get_past_river_gauge_headers(self):
        """ Method: get_past_river_gauge_headers """
        try:
            allheaders = []
            self.click_element(ReadyLivePage.first_past_river_gauge_prediction)
            lst_headers = self.return_object_list(ReadyLivePage.past_river_gauge_headers)
            total = len(lst_headers)
            assert (total/2) == 8, "Expecting a total of 8 past prediction headers!"
            print("List of Past River Gauge Predictions")
            for i in range(total):
                if i % 2 == 0:
                    allheaders.append(lst_headers[i].text)
            assert sorted(allheaders, reverse=True) == allheaders, "Past river gauges NOT in descending order!"
            assert len(allheaders) == len(set(allheaders)), "Found duplicate past river gauge headers!"
            for i in range(len(allheaders)-1):
                end = allheaders[i]
                start = allheaders[i+1]
                print(end, start)
                self.verify_3hr_intervals(start, end)
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get past river gauge headers due to: " + str(error)) from error

    def show_no_past_river_gauge_predictions(self):
        """ Method: show_no_past_river_gauge_predictions """
        try:
            expect = "No past river gauge predictions available."
            actual = self.get_text(ReadyPRGPPage.no_past_river_gauge_predictions_available)
            print(f"Actual text: {actual}")
            assert expect == actual, "Wrong message displayed for no river gauge predictions available!"
        except Exception as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError("Fail to get no past river gauge predictions!") from error
