# URL = 'https://app.isellerpal.com/api-product/best-seller-1000-list'
OPEN_URL='https://app.isellerpal.com/analysis/besetseller'
URL='https://app.isellerpal.com/api-data/performance-dashboard'
# URL = 'http://localhost:8888/video/best-seller-1000-list'
METHOD = 'GET'

Cookie = 'Hm_lvt_3af9f141533380899e8c0acc32b1bcae=1722002528; HMACCOUNT=936E517E1196FE4B; guestId=b6338646d7d54633a479eeb69982ce99; token=eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOjE2MTIxNywic3ViIjoiMTYxMjE3IiwiaWF0IjoxNzIyMDAyNjI4LCJleHAiOjE3MjI2MDc0Mjh9.FQGuwbX1tX64z__WEetsC2jEAkR1wHuvg1IMNPXp--JxGlK5wLRNPfh4vUPH6wI9k50HhukKb0oh0WVSxU6tsg; Hm_lpvt_3af9f141533380899e8c0acc32b1bcae=1722002813'

Headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    # "csrf-token": "0KxVPVi1DUdUpsoWO92EZuvxr+WUK1QZS18rSPllPkM=",
    "isp-token": "eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOjE2MTIxNywic3ViIjoiMTYxMjE3IiwiaWF0IjoxNzIyMDAyNjI4LCJleHAiOjE3MjI2MDc0Mjh9.FQGuwbX1tX64z__WEetsC2jEAkR1wHuvg1IMNPXp--JxGlK5wLRNPfh4vUPH6wI9k50HhukKb0oh0WVSxU6tsg",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "cookie": Cookie,
    "Referer": "https://app.isellerpal.com/analysis/besetseller",
    "Referrer-Policy": "unsafe-url",
    "User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

DATA_RAW = {
    "currentPage": 1,
    "totalPage": 0,
    "pageSize": 50,
    "total": 0,
    "region": "us",
    "id": 20963,
    "sortType": "ascending",
    "sortName": "firstRank",
    "title": "",
    "brandName": "",
    "sellerName": "",
    "shippingType": "",
    "location": "",
    "sizeType": "",
    "includeKeyword": "",
    "excludeKeyword": "",
    "asin": "",
    "hide": True
}

