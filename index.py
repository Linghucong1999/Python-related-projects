import requests
import json
from data import URL, METHOD, Headers, DATA_RAW

session = requests.Session()

response = session.request(method=METHOD, url=URL,
                           headers=Headers, json=DATA_RAW)

# list_data = response.json()['result']
asins_without_price = []

print(response.json())
