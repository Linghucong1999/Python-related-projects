import requests
import json
from data import URL, METHOD, Headers, DATA_RAW

session=requests.Session()
response = session.request(method=METHOD,url=URL,headers=Headers,json=DATA_RAW,params={
'region': 'us'
nodeId: 3741261
})

print(response.text)


