import csv
import requests
import json
import time

apiKey = "7e9fcc5fa8d03177f95f110fd1c05c08"
weather = []  # init the list that will hold all the weather data ==> id: weather API response

f2 = open('hikes_rate5.json',)
test_data = json.load(f2)
weather = test_data
with open('hikes_rate5.csv', 'r') as file:
    with open('hikes_rate5_weather_7days.json', 'w', encoding='utf-8') as f:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            latitude = row[3]
            longitude = row[4]
            response = requests.get("http://api.openweathermap.org/data/2.5/onecall?lat=" + latitude + "&lon=" + longitude + "&exclude=hourly,minutely,alerts" + "&appid=" + apiKey)
            if json.loads(response.text):
                data = json.loads(response.text)
                weather[i]['weather'] = data
            if i % 50 == 0:  # since the API allows only for 60 requests/ min
                print("batch "+str(i)+" is done")
                time.sleep(1)
            i += 1
        json.dump(weather, f, ensure_ascii=False, indent=4)
        f.close()
        f2.close()
