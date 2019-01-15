import api_key
import urllib.request
import json

print("apiKey: " + api_key.KEY)

json_contents = urllib.request.urlopen("https://api.jcdecaux.com/vls/v1/stations?apiKey=" + api_key.KEY +
                                       "&contract=toulouse")

contents = json.load(json_contents)

print(contents)
