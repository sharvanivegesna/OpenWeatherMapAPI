import requests
import datetime

print('enter your city:')
city = input()
print('enter "today","tomorrow" or "week"')
days = input()


response = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=' + city + '&cnt=' + str(
        7) + '&appid=8467a853ab76a8e415b8e7d11f6694a0&units=metric')
j = response.json()

n = 0
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


