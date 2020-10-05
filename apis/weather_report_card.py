"""
Displays a weather report in your current city with current weather conditions and 3 Days Forecast per 5 Hours.

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""
import configparser
import json
import operator
import requests
from datetime import datetime
from tabulate import tabulate

REQUEST_CHOICES = ['current_weather', 'forecast', 'hourly_forecast']
WEATHER_BASE = "https://api.openweathermap.org/data/2.5/"
AP_BASE = "http://api.ipstack.com/check?access_key="
SCREEN_WIDTH = 150
centered = operator.methodcaller('center', SCREEN_WIDTH)


# Helper functions
def get_api_key(category):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[category]['api']


def get_location():
    geo_req = requests.get(f"{AP_BASE}{get_api_key('ap')}")
    return json.loads(geo_req.text)


def display_current_weather(local, lat, lon):
    url = f"{WEATHER_BASE}weather?lat={lat}&lon={lon}&units=metric&appid={get_api_key('weather')}"
    result = requests.get(url).json()

    now = datetime.now()
    print(centered("\nWeather in {}, {} {} ({}) at {}".format(
        local["city"], local["region_name"], local["country_name"], local["zip"], now.strftime("%b %m, %Y %H:%M:%S"))
    ))
    HEADER = ["Wind", "Cloudiness", "Humidity", "Pressure", "Sunrise", "Sunset"]
    contents = [[
        str(result["wind"]["speed"]) + " meter/sec, " + str(result["wind"]["deg"]) + " deg",
        str(result["clouds"]["all"]) + " %",
        str(result["main"]["humidity"]) + " %",
        str(result["main"]["pressure"]) + " hPa",
        get_time(result["sys"]["sunrise"]),
        get_time(result["sys"]["sunset"])
    ]]

    print(centered("Current Weather: {} [{}]".format(
        result['weather'][0]['main'], result['weather'][0]['description']
    )))

    print(centered("Temperature: {} \u00b0C, Feels Like: {} \u00b0C, Minimum: {} \u00b0C / Maximum: {} \u00b0C".format(
        result['main']['temp'], result['main']['feels_like'], result['main']['temp_min'], result['main']['temp_max']
    )))

    print(tabulate(contents, headers=HEADER, tablefmt="fancy_grid"))


def display_forecast(local, lat, lon):
    print(centered("3 Days Forecast / 5 Hours"))
    url = f"{WEATHER_BASE}forecast?lat={lat}&lon={lon}&cnt=20&units=metric&appid={get_api_key('weather')}"
    result = requests.get(url).json()

    HEADER = ["Date and Time", "Status", "Description", "Temperature (\u00b0C)", "Feels Like (\u00b0C)", "Minimum (\u00b0C)", "Maximum (\u00b0C)", "Cloudiness (%)", "Humidity (%)"]
    content = []
    for item in range(result['cnt']):
        root = result['list'][item]
        main = result['list'][item]['main']
        content.append([
            root['dt_txt'],
            root['weather'][0]['main'],
            root['weather'][0]['description'],
            main['temp'],
            main['feels_like'],
            main['temp_min'],
            main['temp_max'],
            root['clouds']['all'],
            main['humidity'],
        ])

    print(tabulate(content, headers=HEADER, tablefmt="grid"))


def get_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%I:%M:%S %p")


if __name__ == "__main__":
    location = get_location()

    display_current_weather(location, location["latitude"], location["longitude"])
    display_forecast(location, location["latitude"], location["longitude"])
