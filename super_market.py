from urllib.request import urlopen, Request, URLError
import requests
import os
import csv
import collections
import time

import xml.etree.ElementTree as ET

api_key = ''

city='Ammon'
state='ID'

cities_in_state = []

# call each function, return the keys of the object as well as the object,
# can I then aggregate all of these things together in one object??


state = 'ID'

def get_cities(api_key):
 
        ############ GET CITY BY STATE #########
    city_payload = {'APIKEY': api_key, 'SelectedState': state,}
    cities = requests.post(
        'http://www.SupermarketAPI.com/api.asmx/CitiesByState', data=city_payload)


    root = 

    for city in cities:
        print(city)



def get_stores(api_key, city, state):


    ##################### GET STORE OBJECT #################3
    store_payload = {'APIKEY': api_key, 'SelectedCity': city, 'SelectedState': state }

    stores = requests.post(
        'http://www.SupermarketAPI.com/api.asmx/StoresByCityState', data=store_payload)

    for store in stores:
        print(store)

get_cities(api_key)

#get_stores(api_key, item, state)



   