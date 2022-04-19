import json
import csv
import urllib.parse
import requests


class EarthQuake:
    def __init__(self, mag, place, time, url, details, tsunami):
        self.alt = None
        self.lon = None
        self.lat = None
        self.mag = mag
        self.place = place
        self.time = time
        self.url = url
        self.details = details
        self.tsunami = tsunami

    def setCoordinates(self, lon, lat, alt):
        self.lon = lon
        self.lat = lat
        self.alt = alt


print("*************************** EarthQuake Data Provider *****************************************")

# 2021-04-01&endtime=2021-09-30&minmag=6&limit=10

while (1):

    st = input("Enter start time: ")
    et = input("Enter end Time: ")
    mm = input("Min Magnitude: ")

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime="
    url += st + "&endtime=" + et + "&minmag=" + mm + "&limit=10"

    json_data = requests.get(url).json()
    # print(json_data)

    json_features = json_data['features']
    #  print(json_features)

    ls = [None] * len(json_features)
    i = 0
    for ele in json_features:
        curF = ele
        prop = curF['properties']
        eq = EarthQuake(prop['mag'], prop['place'], prop['time'], prop['url'], prop['detail'], prop['tsunami'])
        ls[i] = eq
        i += 1
    i = 0
    for ele in ls:
        eq = ele
        print("EarthQuake %d: " % (i + 1))
        print("Mag: ", eq.mag)
        print("place: ", eq.place)
        print("url: ", eq.url)
        print("time: ", eq.time)
        print("Tsunami?: ", eq.tsunami)
        i += 1
        print()

    n = int(input("\nTry Again? 1.Yes 2.Quit:    "))
    if n == 2:
        break
