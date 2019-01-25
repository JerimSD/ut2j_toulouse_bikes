import api_key
import urllib.request
import json
import datetime

timestamp = str(datetime.datetime.now())

print(timestamp, "GET: https://api.jcdecaux.com/vls/v1/stations?apiKey=" + api_key.KEY + "&contract=toulouse")

json_contents = urllib.request.urlopen("https://api.jcdecaux.com/vls/v1/stations?apiKey=" + api_key.KEY +
                                       "&contract=toulouse")

newData = {"timestamp": timestamp, "data": json.load(json_contents)}

with open('/home/jeremy/Documents/M2ICE/UT2J/ut2j_toulouse_bikes/data.json', 'r') as inputFile:
    data = json.load(inputFile)

data.append(newData)

with open('/home/jeremy/Documents/M2ICE/UT2J/ut2j_toulouse_bikes/data.json', 'w') as outputFile:
    json.dump(data, outputFile)
