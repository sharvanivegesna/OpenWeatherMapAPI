
from get_data import GenerateReports

import thread
import time
import matplotlib.pyplot as plt

def trigger_requests(city,country,cnt, lnt, lon):
    time.sleep(15)
    thread.start_new_thread(GenerateReports().get_5day_3h_Report,(city,country))
    thread.start_new_thread(GenerateReports().SixteenDaily,(city, cnt))
    thread.start_new_thread(GenerateReports().current_weather,(lnt, lon))

if __name__ =='__main__':
    while True:
        trigger_requests('london','uk',7,20,20)



