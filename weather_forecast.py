import requests
import json

r = requests.get("http://api.wunderground.com/api/ab78bcbaca641959/forecast/q/Canada/winnipeg.json")
data = r.json()
for day in data['forecast']['simpleforecast']['forecastday']:
    print (day['date']['weekday'] + ":")
    print ("Conditions: ", day['conditions'])
    print ("High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C", '\n')
