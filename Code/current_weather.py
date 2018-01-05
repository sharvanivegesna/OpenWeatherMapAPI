import requests

url = "http://api.openweathermap.org/data/2.5/weather"

querystring = {"lat":"35","lon":"139","appid":"8467a853ab76a8e415b8e7d11f6694a0"}

response = requests.request("GET", url, params=querystring)

print(response.text)