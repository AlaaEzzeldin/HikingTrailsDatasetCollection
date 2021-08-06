import csv
import requests
import json

api_key = "37ce125fbe55bca7093d4786b04f8526"

with open('hikes_Rate5.csv', 'r') as file:
    f = open('locations.csv', 'w')
    writer = csv.writer(f)
    reader = csv.reader(file)
    for row in reader:
        location = row[2].split(",", 1)[0]
        response = requests.get("http://api.positionstack.com/v1/forward?access_key=" +api_key +"&query=" + location)
        if (json.loads(response.text)['data']):
            data = json.loads(response.text)['data'][0]
            exact_location = data['latitude'], data['longitude']
        else:
            exact_location = None, None
        writer.writerow(exact_location)
    f.close()
