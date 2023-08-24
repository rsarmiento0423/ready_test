""" LibraryAPI.py """
#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=E0401

from CommonAPI import (GETEVENTSQUERY, CommonAPI)

variables_library = {
    "collectionFilter": {
        "isLibrary": True
    },
    "offset": 0,
    "limit": 56,
    "order": "Desc",
    "orderField": "UpdateTime"
}

class LibraryAPI(CommonAPI):
    """ Class: LibraryAPI """
    def get_kc_library_events(self):
        """ Method: get_kc_library_events """
        new_cookie = self.get_user_cookies("kcusername", "kcpassword")
        self.get_events(new_cookie, GETEVENTSQUERY, variables_library)

    def get_chiba_library_events(self):
        """ Method: get_chiba_library_events """
        new_cookie = self.get_user_cookies("chibausername", "chibapassword")
        self.get_events(new_cookie, GETEVENTSQUERY, variables_library)

    def get_kawasaki_library_events(self):
        """ Method: get_kawasaki_library_events """
        new_cookie = self.get_user_cookies("kawasakiusername", "kawasakipassword")
        self.get_events(new_cookie, GETEVENTSQUERY, variables_library)

    def get_koriyama_library_events(self):
        """ Method: get_koriyama_library_events """
        new_cookie = self.get_user_cookies("koriyamausername", "koriyamapassword")
        self.get_events(new_cookie, GETEVENTSQUERY, variables_library)

    def get_nagano_library_events(self):
        """ Method: get_nagano_library_events """
        new_cookie = self.get_user_cookies("naganousername", "naganopassword")
        self.get_events(new_cookie, GETEVENTSQUERY, variables_library)

    def get_okayama_library_events(self):
        """ Method: get_okayama_library_events """
        new_cookie = self.get_user_cookies("okayamausername", "okayamapassword")
        self.get_events(new_cookie, GETEVENTSQUERY, variables_library)

    def get_okazaki_library_events(self):
        """ Method: get_okazaki_library_events """
        new_cookie = self.get_user_cookies("okazakiusername", "okazakipassword")
        self.get_events(new_cookie, GETEVENTSQUERY, variables_library)
