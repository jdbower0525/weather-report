import requests
import json

# key id = 6747d8c3dbb46cec


class CurrentConditions:

    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.url = (
         "http://api.wunderground.com/api/6747d8c3dbb46cec/conditions/q/{}.json"
         .format(self.zip_code))

    def current_conditions(self):
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))


class TenDayForecast:
    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.url = (
         "http://api.wunderground.com/api/6747d8c3dbb46cec/forecast10day/q/{}.json"
         .format(self.zip_code, '.json')
         )

    def tenday_forecast(self):
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))


class SunRiseSunSet:
    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.url = (
         "http://api.wunderground.com/api/6747d8c3dbb46cec/astronomy/q/{}.json"
         .format(self.zip_code))

    def sunrise_sunset(self):
        r = requests.get(self.url)
        results = r.json()
        sun_phase = results["sun_phase"]
        print("Sunrise = {}:{}\nSunset = {}:{}".format(
            sun_phase["sunrise"]["hour"],
            sun_phase["sunrise"]["minute"],
            sun_phase["sunset"]["hour"],
            sun_phase["sunset"]["minute"]))


class Alerts:
    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.url = (
         "http://api.wunderground.com/api/6747d8c3dbb46cec/alerts/q/{}.json"
         .format(self.zip_code))

    def alert(self):
        r = requests.get(self.url)
        results = r.json()
        if len(results["alerts"]) == 0:
            print("No severe weather alerts for your area. ")
        else:
            print(json.dumps(r.json(), indent=4))


class Hurricane:
    def __init__(self):
        self.url = (
            "http://api.wunderground.com/api/6747d8c3dbb46cec/currenthurricane/view.json"
            )

    def hurricane(self):
        r = requests.get(self.url)
        results = r.json()
        currenthurricane = results['currenthurricane']
        print(currenthurricane[0]['stormInfo']["stormName_Nice"])
