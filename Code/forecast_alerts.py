import requests

url = "http://api.openweathermap.org/data/3.0/triggers"

querystring = ( )

response = requests.request("GET", url, params=querystring)

print(response.text)