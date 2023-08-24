""" CommonAPI.py """
#pylint: disable=C0301
#pylint: disable=C0103

import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

GETEVENTSQUERY = """
query GetEvents($collectionFilter: HazardCollectionFilter = {}, $offset: Int = 0, $limit: Int = 56, $order: Direction = Desc, $orderField: HazardSortingField = UpdateTime) {
  hazardEvents(
    offset: $offset
    limit: $limit
    hazardfilter: {floodHazardFilter: {severity: Normal, atPeakTime: true}}
    collectionfilter: $collectionFilter
    orderBy: [{field: $orderField, direction: $order}]
  ) {
    id
    status
    predictionStatus
    startTime
    endTime
    updatedAt
    createdAt
    hazardType
    eventType
    name
    customName
    isArchived
    ...starPrediction
    floodEventMetadata {
      id
      peakTime
      damage {
        id
        waterDepthStats {
          maxWaterDepth
          maxInundatedArea
          buildingsImpactedPerDepth
          peopleImpacted
          __typename
        }
        __typename
      }
      __typename
    }
    seismicEventMetadata {
      location
      faultName
      magnitude
      depth
      epicenter {
        coordinates
        __typename
      }
      damage {
        impactStats {
          people {
            total
            __typename
          }
          buildings {
            total
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment starPrediction on HazardEvent {
  isStarred
  disappearIfUnstarred
  __typename
}    
"""

def extract_cookie(all_cookies):
    """ Function: extract_cookie
        Extracting values: _ga, _gid, kc-access, kc-state _gat_UA-75555102-3, _gat_UA-75555102-4, _dd_s,
        intercom-session-ywb3kjn1
    """
    lst1 = []
    # print("Total cookies: {}".format(len(all_cookies)))
    for cookie in all_cookies:
        # print("Got cookie: {}\n".format(cookie))
        for key in cookie.keys():
            # print("key: {}, value: {}".format(key, cookie[key]))
            if key == 'name' and cookie[key] == '_gid':
                # print("Got _gid:", cookie['value'])
                lst1.append("_gid=" + str(cookie['value']))
            if key == 'name' and cookie[key] == '_ga':
                # print("Got _ga:", cookie['value'])
                lst1.append("_ga=" + str(cookie['value']))
            if key == 'name' and cookie[key] == '_gat_UA-75555102-3':
                # print("Got _gat_UA-75555102-3:", cookie['value'])
                lst1.append("_gat_UA-75555102-3=" + str(cookie['value']))
            if key == 'name' and cookie[key] == '_gat_UA-75555102-4':
                # print("Got _gat_UA-75555102-4:", cookie['value'])
                lst1.append("_gat_UA-75555102-4=" + str(cookie['value']))
            if key == 'name' and cookie[key] == '_dd_s':
                # print("Got _dd_s:", cookie['value'])
                lst1.append("_dd_s=" + str(cookie['value']))
            if key == 'name' and cookie[key] == 'intercom-session-ywb3kjn1':
                # print("Got intercom-session-ywb3kjn1:", cookie['value'])
                lst1.append("intercom-session-ywb3kjn1=" + str(cookie['value']))
            if key == 'name' and cookie[key] == 'kc-access':
                # print("Got kc-access:", cookie['value'])
                lst1.append("kc-access=" + str(cookie['value']))
            if key == 'name' and cookie[key] == 'kc-state':
                # print("Got kc-state:", cookie['value'])
                lst1.append("kc-state=" + str(cookie['value']))

    new_cookie = "; ".join(sorted(lst1))
    # print("New cookie:{}".format(new_cookie))
    return new_cookie

class CommonAPI():
    """ Class: CommonAPI """

    def __init__(self):
        self.accounts_file = "./data/accounts.json"
        self.PLAYGROUND_URL = 'https://app.staging.onec.co/query?'
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=chrome_options)

    def login_ready(self, url, username, password):
        """ Method: login_ready """
        self.driver.get(url)
        self.driver.implicitly_wait(5)

        page_title = self.driver.title
        print("Login Page title: {}".format(page_title))
        assert page_title == "One Concern", "Expected 'One Concern' for page title!"

        self.driver.switch_to.frame('login-iframe')
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

        page_title = self.driver.title
        print("Home Page title: {}".format(page_title))
        assert page_title == "One Concern", "Expected 'One Concern' for page title!"
        print("Logged into One Concern as: {}".format(username))
        all_cookies = self.driver.get_cookies()
        self.driver.quit()
        return all_cookies

    def get_events(self, cookie, myquery, myvars):
        """ Method: get_library_events """
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'cookie': cookie}
        resp = requests.post(self.PLAYGROUND_URL, headers=headers, json={'query': myquery, 'variables': myvars})
        assert resp.status_code == 200, "Expected 200 status code!"
        data = resp.json()
        print(json.dumps(data, indent=2))
        tot_hazard_events = len(data["data"]["hazardEvents"])
        print("Got total hazard events found: {}".format(tot_hazard_events))
        lst_eventids = []
        for i in range(tot_hazard_events):
            event_id = data["data"]["hazardEvents"][i]["id"]
            lst_eventids.append(event_id)
            print("Hazard event_id: {}".format(event_id))
        return lst_eventids

    def get_user_cookies(self, username, password):
        """ Method: get_user_cookies """
        with open(self.accounts_file) as file:
            data = json.load(file)
        all_cookies = self.login_ready("https://app.staging.onec.co/#/home", data[username], data[password])
        new_cookie = extract_cookie(all_cookies)
        return new_cookie

    def get_expect_river_gauges(self, rivergaugename):
        """ Method: get_expect_river_gauges """
        with open(self.accounts_file) as file:
            data = json.load(file)
        river_gauge_name = data.get(rivergaugename)
        return river_gauge_name
