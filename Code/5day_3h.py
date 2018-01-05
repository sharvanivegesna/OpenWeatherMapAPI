import requests
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read('config.ini')

class GenerateReports(object):
    def __init__(self):
        self.url = Config.get('settings','url')
        self.APPID = Config.get('settings','APPID')

    def get_response(self, url, params):

        response = requests.request("GET", url, params=params)
        result = response.text
        return result

    def get_5day_3h_Report(self, city, country):
        url = self.url + "/data/2.5/forecast"

        querystring = {"q":"{city},{country}".format(city=city,country=country),"mode":"json","APPID":self.APPID}
        result = self.get_response(url, querystring)
        return result


    def SixteenDaily(self,city, cnt ):
        url = self.url + "/data/2.5/forecast/daily"

        querystring = {"q": "{city}".format(city=city), "mode": "json", "units": "metric", "cnt": "{cnt}".format(cnt=cnt),
                       "APPID": self.APPID}
        result = self.get_response(url, querystring)
        return result

    def current_weather(self, lat, lon):
        url = self.url + "/data/2.5/weather"

        querystring = {"lat": lat, "lon": lon, "appid": self.APPID}
        result = self.get_response(url, querystring)
        return result