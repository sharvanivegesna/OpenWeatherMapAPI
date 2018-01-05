from threading import Thread
import requests
import json
import urllib.request
import datetime


class Forecast():
    date = datetime.datetime()
    predictions = []

class Prediction():
    min_temp = ""
    max_temp = ""
    weather = ""

def get_today_weather(city_code):

    response = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=' + city_code + '&cnt=' + str(
        7) + '&appid=8467a853ab76a8e415b8e7d11f6694a0&units=metric')
    j = response.json()

def get_forecast(code):
    pass

def get_daily_forecast(code):
    pass

def read_configuration_file(code):
    pass

from _thread import start_new_thread
start_new_thread(get_forecast,('asjkdhf123'))
start_new_thread(get_daily_forecast,('asjkdhf123'))
start_new_thread(get_today_weather,('asjkdhf123'))

days = ''
if days == 'week':
     while n < 7:
        udate = j["list"][n]["dt"]
        date = datetime.datetime.fromtimestamp(int(udate)).strftime('%d-%m-%Y')
        temp_min = j["list"][n]["temp"]["min"]
        temp_max = j["list"][n]["temp"]["max"]
        weather =  j["list"][n]["weather"][0]["description"]
        print("date")
        print("Temp min"+  str(temp_min))
        print("Temp max" + str(temp_max))
        print("weather:" + weather)
        print("-========-")
        n = n + 1
elif days == 'tomorrow':
    udate = j["list"][1]["dt"]
    date = datetime.datetime.fromtimestamp(int(udate)).strftime('%d-%m-%Y')
    temp_min = j["list"][1]["temp"]["min"]
    temp_max = j["list"][1]["temp"]["max"]
    weather = j["list"][1]["weather"][0]["description"]
    print("date")
    print("Temp min" + str(temp_min))
    print("Temp max" + str(temp_max))
    print("weather:" + weather)

elif days == 'today':
    udate = j["list"][0]["dt"]
    date = datetime.datetime.fromtimestamp(int(udate)).strftime('%d-%m-%Y')
    temp_min = j["list"][0]["temp"]["min"]
    temp_max = j["list"][0]["temp"]["max"]
    weather = j["list"][0]["weather"][0]["description"]
    print("date")
    print("Temp min" + str(temp_min))
    print("Temp max" + str(temp_max))
    print("weather:" + weather)
