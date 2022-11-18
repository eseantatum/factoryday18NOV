import requests
import datetime
import time
import random
import json

class weatherForecaster:
    def __init__(self):
        self.APIKey = "3faf1d1d4c95245aff49d70ebaf587b9"
        self.lat = "40.441119"
        self.long = "-80.005722"
        
    
    def getCurrentWeather(self):
        APIcall = "https://api.openweathermap.org/data/2.5/weather?lat=" + self.lat + "&lon=" + self.long + "&appid=" + self.APIKey
        response = requests.get(APIcall)
        print(response.json().get("main"))
        return response.json().get("main")
        
        
    def getHistoricWeather(self, year, month, day):
       timeRequest = datetime.datetime(year, month, day, 0, 0)
       timeStamp = str(time.mktime(timeRequest.timetuple()))
       #print(timeStamp)
       APIcall = "https://history.openweathermap.org/data/2.5/history/city?lat=" + self.lat + "&lon=" + self.long + "&type=hour&start=" + timeStamp + "&cnt={cnt}&appid=" + self.APIKey
       response = requests.get(APIcall)
       print(response.json())
       return response.json().get("main")
       
    def getHistoricCheat(self, year, month, day):
        noise = random.randrange(-10,10)
        #print(noise)
        temp = 2 + noise
        dict = {
        "temp":temp,
        "feels_like":temp,
        "temp_min": temp - abs(noise * 2),
        "temp_max": temp + abs(noise*2),
        "pressure": 1019,
        "humidity": 83
        }
        #print(dict)
        return json.dumps(dict)
        
    
    
    def aggregate(self, dates):
        dict = {}
        for date in dates:
            res = self.getHistoricCheat(date[0],date[1],date[2])
            dict[datetime.datetime(date[0],date[1],date[2], 0, 0).strftime("%Y-%m-%d")] = res
            
        return json.dumps(dict)
    

#forecast = weatherForecaster()
#forecast.getCurrentWeather()
#forecast.getHistoricWeather(2020, 11, 21)
#forecast.getHistoricCheat(202, 11, 21)
#dateList = [ [2020,11,21], [2019,11,21], [2018,11,21] ]
#forecast.aggregate(dateList)
