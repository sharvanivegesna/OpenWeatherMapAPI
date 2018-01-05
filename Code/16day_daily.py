import requests

url = "http://api.openweathermap.org/data/2.5/forecast/daily"

querystring = {"q":"London","mode":"json","units":"metric","cnt":"7","APPID":"8467a853ab76a8e415b8e7d11f6694a0"}


response = requests.request("GET", url, params=querystring)

print(response.text)