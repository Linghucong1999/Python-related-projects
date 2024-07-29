URL = 'https://app.isellerpal.com/api-product/best-seller-1000-list'
OPEN_URL = 'https://app.isellerpal.com/analysis/besetseller'
# URL = 'https://app.isellerpal.com/api-data/performance-dashboard'
# URL = 'http://localhost:8888/video/best-seller-1000-list'
METHOD = 'POST'

Cookie = 'Hm_lvt_3af9f141533380899e8c0acc32b1bcae=1722215569; HMACCOUNT=8436478169709B3C; guestId=1e4bb37b6ffc456b85741444fe19c268; token=eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOjE2MTIxNywic3ViIjoiMTYxMjE3IiwiaWF0IjoxNzIyMjE1NjE1LCJleHAiOjE3MjI4MjA0MTV9.oPvBQ2oPKLW9hbvLRuiaeK98d9wp1-2cvJX7hdla6D6fFoJXYbdPGvbnEA8VyRHyjZPyW1zFFF325kL10_P1IA; Hm_lpvt_3af9f141533380899e8c0acc32b1bcae=1722215802'

Headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "csrf-token": "4KWq41BNtTOLkOSClLXRWD8aRKuOTpgX2Bnzzpupb2M=",
    "isp-token": "eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOjE2MTIxNywic3ViIjoiMTYxMjE3IiwiaWF0IjoxNzIyMjE1NjE1LCJleHAiOjE3MjI4MjA0MTV9.oPvBQ2oPKLW9hbvLRuiaeK98d9wp1-2cvJX7hdla6D6fFoJXYbdPGvbnEA8VyRHyjZPyW1zFFF325kL10_P1IA",
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
    "User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
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
