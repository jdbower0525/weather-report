import requests

# key id = 6747d8c3dbb46cec


class CurrentConditions:

    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.url = (
         "http://api.wunderground.com/api/6747d8c3dbb46cec/conditions/q/{}.json"
         .format(self.zip_code))

    def current_conditions(self):
        r = requests.get(self.url)
        results = r.json()
        location = results["current_observation"]["display_location"]["full"]
        weather = results["current_observation"]["weather"]
        temp = results["current_observation"]["temperature_string"]
        humidity = results["current_observation"]["relative_humidity"]
        wind_strength = results["current_observation"]["wind_string"]
        print("""
Your City: {}
Weather: {}
Temperature: {}
Humidity: {}
Wind Strength: {}
    """.format(location, weather, temp, humidity, wind_strength))


class TenDayForecast:
    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.url = (
         "http://api.wunderground.com/api/6747d8c3dbb46cec/forecast10day/q/{}.json"
         .format(self.zip_code, '.json')
         )

    def tenday_forecast(self):
        r = requests.get(self.url)
        results = r.json()
        i = 0
        while i < 20:
            daily = results["forecast"]["txt_forecast"]["forecastday"][i]
            period = daily['title']
            forecast = daily['fcttext']
            print("""
Period: {}
Forecast: {}
            """.format(period, forecast))
            i += 1


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
            print(results['alerts'][0]['expires'])
            print('\n')
            message = results['alerts'][0]['message']
            strip_message = message.strip('\n')
            print(strip_message)
            print('\n')


class Hurricane:
    def __init__(self):
        self.url = (
            "http://api.wunderground.com/api/6747d8c3dbb46cec/currenthurricane/view.json"
            )

    def hurricane(self):
        r = requests.get(self.url)
        results = r.json()
        try:
            currenthurricane = results['currenthurricane']
            print(currenthurricane[0]['stormInfo']["stormName_Nice"])
        except:
            print("There are no hurricanes currently.")
