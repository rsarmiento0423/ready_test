""" RiverGaugesAPI.py """
#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=E0401
#pylint: disable=R0914

import requests
import yaml
from CommonAPI import CommonAPI

GETLATESTPOIDETAILS = """
query GetLastPoiDetails {
  floodPoiDetails {
    id
    category
    location {
      type
      coordinates
      __typename
    }
    name
    labels
    thresholds {
      threshold
      labels
      __typename
    }
    stats {
      id
      timestamp
      depth
      __typename
    }
    __typename
  }
}
"""

def compare_data(output, geo):
    """ Function: compare_data """
    yamlfile = "./data/river_gauges.yaml"
    with open(yamlfile, 'r') as file:
        ddata = yaml.safe_load(file)

    total_river_gauges = len(ddata[geo])
    for i in range(total_river_gauges):
        expect_rivergauge_name = ddata[geo][i]["river_gauge_name"]
        actual_rivergauge_name = output["data"]["floodPoiDetails"][i]["name"]
        print(f"Actual river gauge name: {actual_rivergauge_name}")
        assert expect_rivergauge_name == actual_rivergauge_name, f"Expect: {expect_rivergauge_name} Got: {actual_rivergauge_name} river gauge name!"
        expect_poi_id = ddata[geo][i]["poi_id"]

        if geo == "kc":
            actual_poi_id = output["data"]["floodPoiDetails"][i]["id"][:1]
            print(f"Actual poi_id: {actual_poi_id}")
            assert expect_poi_id == actual_poi_id, f"Expect: {expect_poi_id} Got: {actual_poi_id} poi_id!"
        else:
            actual_poi_id = output["data"]["floodPoiDetails"][i]["id"][:6]
            print(f"Actual poi_id: {actual_poi_id}")
            assert expect_poi_id == actual_poi_id, f"Expect: {expect_poi_id} Got: {actual_poi_id} poi_id!"

        expect_city_name = ddata[geo][i]["city_name"]
        actual_city_name = output["data"]["floodPoiDetails"][i]["labels"]["city_name"]
        print(f"Actual city name: {actual_city_name}")
        assert expect_city_name == actual_city_name, f"Expect: {expect_city_name} Got: {actual_city_name} city name!"

        expect_gauge_id = ddata[geo][i]["gauge_id"]
        actual_gauge_id = output["data"]["floodPoiDetails"][i]["labels"]["gauge_id"]
        print(f"Actual gauge_id: {actual_gauge_id}")
        assert expect_gauge_id == actual_gauge_id, f"Expect: {expect_gauge_id} Got: {actual_gauge_id} gauge_id!"

        expect_mlit_link = ddata[geo][i]["mlit_link"]
        actual_mlit_link = output["data"]["floodPoiDetails"][i]["labels"]["mlit_link"]
        print(f"Actual mlit_link: : {actual_mlit_link}")
        assert expect_mlit_link == actual_mlit_link, f"Expect: {expect_mlit_link} Got: {actual_mlit_link} mlit!"

        expect_river_name = ddata[geo][i]["river_name"]
        actual_river_name = output["data"]["floodPoiDetails"][i]["labels"]["river_name"]
        print(f"Actual river name: {actual_river_name}")
        assert expect_river_name == actual_river_name, f"Expect: {expect_river_name} Got: {actual_river_name} river name!"

        expect_station = ddata[geo][i]["station"]
        actual_station = output["data"]["floodPoiDetails"][i]["labels"]["station"]
        print(f"Actual station: {actual_station}")
        assert expect_station == actual_station, f"Expect: {expect_station} Got: {actual_station} station!"

class RiverGaugesAPI(CommonAPI):
    """ Class: RiverGaugesAPI """
    def verify_kc_river_gauges(self):
        """ Method: verify_kc_river_gauges """
        new_cookie = self.get_user_cookies("kcusername", "kcpassword")
        headers = {'Content-Type': 'application/json', 'cookie': new_cookie}

        # Verify KC river gauges
        resp = requests.post(self.PLAYGROUND_URL, headers=headers, json={'query': GETLATESTPOIDETAILS}, timeout=10)
        assert resp.status_code == 200, "Expected 200 status code!"
        output = resp.json()
        # print(json.dumps(output, ensure_ascii=False, indent=2))
        actual_river_gauges = len(output["data"]["floodPoiDetails"])
        print("Got total river gauges KC found: {}".format(actual_river_gauges))
        expected = self.get_expect_river_gauges("kc_river_gauges")
        assert actual_river_gauges == expected, "Expected {} total river gauges!".format(expected)
        compare_data(output, "kc")

    def verify_chiba_river_gauges(self):
        """ Method: verify_chiba_river_gauges """
        new_cookie = self.get_user_cookies("chibausername", "chibapassword")
        headers = {'Content-Type': 'application/json', 'cookie': new_cookie}

        # Verify Chiba river gauges
        resp = requests.post(self.PLAYGROUND_URL, headers=headers, json={'query': GETLATESTPOIDETAILS}, timeout=10)
        assert resp.status_code == 200, "Expected 200 status code!"
        output = resp.json()
        # print(json.dumps(output, indent=2))
        actual_river_gauges = len(output["data"]["floodPoiDetails"])
        print("Got total river gauges Chiba found: {}".format(actual_river_gauges))
        expected = self.get_expect_river_gauges("chiba_river_gauges")
        assert actual_river_gauges == expected, "Expected {} total river gauges!".format(expected)

    def verify_kawasaki_river_gauges(self):
        """ Method: verify_kawasaki_river_gauges """
        new_cookie = self.get_user_cookies("kawasakiusername", "kawasakipassword")
        headers = {'Content-Type': 'application/json', 'cookie': new_cookie}

        # Verify Kawasaki river gauges
        resp = requests.post(self.PLAYGROUND_URL, headers=headers, json={'query': GETLATESTPOIDETAILS}, timeout=10)
        assert resp.status_code == 200, "Expected 200 status code!"
        output = resp.json()
        # print(json.dumps(output, indent=2))
        actual_river_gauges = len(output["data"]["floodPoiDetails"])
        print("Got total river gauges Kawasaki found: {}".format(actual_river_gauges))
        expected = self.get_expect_river_gauges("kawasaki_river_gauges")
        assert actual_river_gauges == expected, "Expected {} total river gauges!".format(expected)
        compare_data(output, "kawasaki")

    def verify_koriyama_river_gauges(self):
        """ Method: verify_koriyama_river_gauges """
        new_cookie = self.get_user_cookies("koriyamausername", "koriyamapassword")
        headers = {'Content-Type': 'application/json', 'cookie': new_cookie}

        # Verify Koriyama river gauges
        resp = requests.post(self.PLAYGROUND_URL, headers=headers, json={'query': GETLATESTPOIDETAILS}, timeout=10)
        assert resp.status_code == 200, "Expected 200 status code!"
        output = resp.json()
        # print(json.dumps(output, indent=2))
        actual_river_gauges = len(output["data"]["floodPoiDetails"])
        print("Got total river gauges Koriyama found: {}".format(actual_river_gauges))
        expected = self.get_expect_river_gauges("koriyama_river_gauges")
        assert actual_river_gauges == expected, "Expected {} total river gauges!".format(expected)
        compare_data(output, "koriyama")

    def verify_nagano_river_gauges(self):
        """ Method: verify_nagano_river_gauges """
        new_cookie = self.get_user_cookies("naganousername", "naganopassword")
        headers = {'Content-Type': 'application/json', 'cookie': new_cookie}

        # Verify Nagano river gauges
        resp = requests.post(self.PLAYGROUND_URL, headers=headers, json={'query': GETLATESTPOIDETAILS}, timeout=10)
        assert resp.status_code == 200, "Expected 200 status code!"
        output = resp.json()
        # print(json.dumps(output, indent=2))
        actual_river_gauges = len(output["data"]["floodPoiDetails"])
        print("Got total river gauges Nagano found: {}".format(actual_river_gauges))
        expected = self.get_expect_river_gauges("nagano_river_gauges")
        assert actual_river_gauges == expected, "Expected {} total river gauges!".format(expected)
        compare_data(output, "nagano")

    def verify_okayama_river_gauges(self):
        """ Method: verify_okayama_river_gauges """
        new_cookie = self.get_user_cookies("okayamausername", "okayamapassword")
        headers = {'Content-Type': 'application/json', 'cookie': new_cookie}

        # Verify Okayama river gauges
        resp = requests.post(self.PLAYGROUND_URL, headers=headers, json={'query': GETLATESTPOIDETAILS}, timeout=10)
        assert resp.status_code == 200, "Expected 200 status code!"
        output = resp.json()
        # print(json.dumps(output, indent=2))
        actual_river_gauges = len(output["data"]["floodPoiDetails"])
        print("Got total river gauges Okayama found: {}".format(actual_river_gauges))
        expected = self.get_expect_river_gauges("okayama_river_gauges")
        assert actual_river_gauges == expected, "Expected {} total river gauges!".format(expected)
        compare_data(output, "okayama")

    def verify_okazaki_river_gauges(self):
        """ Method: verify_okazaki_river_gauges """
        new_cookie = self.get_user_cookies("okazakiusername", "okazakipassword")
        headers = {'Content-Type': 'application/json', 'cookie': new_cookie}

        # Verify Okazaki river gauges
        resp = requests.post(self.PLAYGROUND_URL, headers=headers, json={'query': GETLATESTPOIDETAILS}, timeout=10)
        assert resp.status_code == 200, "Expected 200 status code!"
        output = resp.json()
        # print(json.dumps(output, indent=2))
        actual_river_gauges = len(output["data"]["floodPoiDetails"])
        print("Got total river gauges Okazaki found: {}".format(actual_river_gauges))
        expected = self.get_expect_river_gauges("okazaki_river_gauges")
        assert actual_river_gauges == expected, "Expected {} total river gauges!".format(expected)
        compare_data(output, "okazaki")
