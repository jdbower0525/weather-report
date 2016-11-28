from api_endpoints import CurrentConditions
from api_endpoints import TenDayForecast
from api_endpoints import SunRiseSunSet


def redirect():
    redirect = input("Would you like to (s)earch again or (e)xit? ")
    if redirect[0] == 's':
        main()
    else:
        exit()


def current_conditions(zip_code):
    cc = CurrentConditions(zip_code)
    cc.current_conditions()
    redirect()


def tendayforecast(zip_code):
    tenday = TenDayForecast(zip_code)
    tenday.tenday_forecast()
    redirect()


def sunrise_sunset(zip_code):
    phase = SunRiseSunSet(zip_code)
    phase.sunrise_sunset()
    redirect()


def main():
    zip_code = input("What zip code would you like to find the weather for? ")
    options = input("""
What report would you like?
1) Current Conditions
2) Ten Day Forecast
3) Sunrise/Sunset
4) Current Weather Alerts
5) Hurricane Update

>>> """)
    if options == '1':
        current_conditions(zip_code)
    if options == '2':
        tendayforecast(zip_code)
    if options == '3':
        sunrise_sunset(zip_code)

main()