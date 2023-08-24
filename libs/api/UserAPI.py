""" UserAPI.py """
#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=E0401

import json
import requests
from CommonAPI import CommonAPI

GETCURRENTUSERQUERY = """
    query GetCurrentUser {
      user {
        ...userDetails
        __typename
      }
    }

    fragment userDetails on User {
      id
      role
      title
      personalInfo {
        firstName
        lastName
        contact {
          email
          phoneNumber
          __typename
        }
        __typename
      }
      status
      preferences {
        language
        countryCode
        country
        timezone
        units
        __typename
      }
      __typename
    }
"""

class UserAPI(CommonAPI):
    """ Class: UserAPI """
    def get_current_user(self, cookie):
        """ Method: get_current_user """
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'cookie': cookie}
        resp = requests.post(self.PLAYGROUND_URL, headers=headers, json={'query': GETCURRENTUSERQUERY})

        assert resp.status_code == 200, "Expected 200 status code!"
        data = resp.json()
        print(json.dumps(data, indent=2))

    def get_kc_user(self):
        """ Method: get_kc_user """
        new_cookie = self.get_user_cookies("kcusername", "kcpassword")
        self.get_current_user(new_cookie)

    def get_chiba_user(self):
        """ Method: get_chiba_user """
        new_cookie = self.get_user_cookies("chibausername", "chibapassword")
        self.get_current_user(new_cookie)

    def get_kawasaki_user(self):
        """ Method: get_kawasaki_user """
        new_cookie = self.get_user_cookies("kawasakiusername", "kawasakipassword")
        self.get_current_user(new_cookie)

    def get_koriyama_user(self):
        """ Method: get_koriyama_user """
        new_cookie = self.get_user_cookies("koriyamausername", "koriyamapassword")
        self.get_current_user(new_cookie)

    def get_nagano_user(self):
        """ Method: get_nagano_user """
        new_cookie = self.get_user_cookies("naganousername", "naganopassword")
        self.get_current_user(new_cookie)

    def get_okayama_user(self):
        """ Method: get_okayama_user """
        new_cookie = self.get_user_cookies("okayamausername", "okayamapassword")
        self.get_current_user(new_cookie)

    def get_okazaki_user(self):
        """ Method: get_okazaki_user """
        new_cookie = self.get_user_cookies("okazakiusername", "okazakipassword")
        self.get_current_user(new_cookie)
