from api_endpoints import CurrentConditions
from api_endpoints import TenDayForecast
from api_endpoints import SunRiseSunSet
from api_endpoints import Alerts
from api_endpoints import Hurricane
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def redirect(zip_code):
    redirect = input("Would you like to (s)earch again,"
                     " (c)hange zip or (e)xit? ")
    if redirect[0] == 's':
        user_input(zip_code)
    elif redirect[0] == 'c':
        main()
    else:
        exit()


def current_conditions(zip_code):
    cc = CurrentConditions(zip_code)
    cc.current_conditions()
    redirect(zip_code)


def tendayforecast(zip_code):
    tenday = TenDayForecast(zip_code)
    tenday.tenday_forecast()
    redirect(zip_code)


def sunrise_sunset(zip_code):
    phase = SunRiseSunSet(zip_code)
    phase.sunrise_sunset()
    redirect(zip_code)


def alerts(zip_code):
    alert = Alerts(zip_code)
    alert.alert()
    redirect(zip_code)


def hurricane(zip_code):
    hurricane = Hurricane()
    hurricane.hurricane()
    redirect(zip_code)


def user_input(zip_code):
    clear()
    options = input("""
What report would you like?
1) Current Conditions
2) Ten Day Forecast
3) Sunrise/Sunset
4) Current Weather Alerts
5) Hurricane Update
6) Exit

>>> """)
    if options == '1':
        current_conditions(zip_code)
    elif options == '2':
        tendayforecast(zip_code)
    elif options == '3':
        sunrise_sunset(zip_code)
    elif options == '4':
        alerts(zip_code)
    elif options == '5':
        hurricane(zip_code)
    else:
        exit()


def main():
    clear()
    zip_code = input("What zip code would you like to find the weather for? ")
    user_input(zip_code)
main()
