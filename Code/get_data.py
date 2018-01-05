import requests
import ConfigParser
import db
import json
import numpy
import matplotlib.pyplot as plt

Config = ConfigParser.ConfigParser()
Config.read('config.ini')

class GenerateReports(object):
    def __init__(self):
        self.url = Config.get('settings','url')
        self.APPID = Config.get('settings','APPID')



    def plot(self,data):
        min = []
        max = []
        dates = []
        for prediction in data["list"]:
            print prediction
            min.append(prediction["temp"]["min"])
            max.append(prediction["temp"]["max"])
            dates.append(prediction["dt"])

        N = len(min)
        men_means = min
        ind = numpy.arange(N)  # the x locations for the groups
        width = 0.35  # the width of the bar
        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, men_means, width, color='r')
        women_means = max
        rects2 = ax.bar(ind + width, women_means, width, color='y')

        # add some text for labels, title and axes ticks
        ax.set_ylabel('Temperature')
        ax.set_title('Minimum and Maximum temp')
        ax.set_xticks(ind + width / 2)

        datesArray = []
        for date in dates:
            datesArray.append(self.stringFromDate(date))
        ax.set_xticklabels(datesArray)

        ax.legend((rects1[0], rects2[0]), ('Min', 'Max'))

        plt.show()

    def stringFromDate(self,dateWeird):
        #complete the code here

        return dateWeird

    def get_response(self, url, params):

        response = requests.request("GET", url, params=params)
        result = response.text
        return result

    def get_5day_3h_Report(self, city, country):
        url = self.url + "/data/2.5/forecast"

        querystring = {"q":"{city},{country}".format(city=city,country=country),"mode":"json","APPID":self.APPID}
        try:
            result = self.get_response(url, querystring)
        except:
            return False
        db.post_data(json.loads(result),'5daydata')
        #print type(json.loads(result))
        return True


    def SixteenDaily(self,city, cnt ):
        url = self.url + "/data/2.5/forecast/daily"

        querystring = {"q": "{city}".format(city=city), "mode": "json", "units": "metric", "cnt": "{cnt}".format(cnt=cnt),
                       "APPID": self.APPID}
        try:
            result = self.get_response(url, querystring)
        except:
            return False
        db.post_data(json.loads(result),'16daydata')

        p = json.loads(result)
        self.plot(p)
        print(p)
        input()

        print result
        return True

    def current_weather(self, lat, lon):
        url = self.url + "/data/2.5/weather"

        querystring = {"lat": lat, "lon": lon, "appid": self.APPID}
        try:
            result = self.get_response(url, querystring)
        except:
            return False
        db.post_data(json.loads(result),'currentdata')
        print result
        return True
GenerateReports().get_5day_3h_Report(city='london',country='us')




