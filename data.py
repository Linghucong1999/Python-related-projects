import os

URL = 'https://app.isellerpal.com/api-product/best-seller-1000-list'
METHOD = 'POST'

# 加密数据传输
csrf_token = os.popen('node ./index.js').read().strip()

isp_token = 'eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOjE2MTIxNywic3ViIjoiMTYxMjE3IiwiaWF0IjoxNzIyNjA3NTU0LCJleHAiOjE3MjMyMTIzNTR9.spVdmeC8FINw3Fi9eKfcTQ_Zkw_PnPoy813ydy0iHrlotsrh1cdz5WdBCbe-R3akSWgjayca9X8Tzpv3o1rTDA'
cookies = 'guestId=b6338646d7d54633a479eeb69982ce99; Hm_lvt_282b3ee77c50ff5447b7b85d121a397d=1722082749; Hm_lvt_3af9f141533380899e8c0acc32b1bcae=1722002528,1722349973,1722607547; HMACCOUNT=936E517E1196FE4B; token=eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOjE2MTIxNywic3ViIjoiMTYxMjE3IiwiaWF0IjoxNzIyNjA3NTU0LCJleHAiOjE3MjMyMTIzNTR9.spVdmeC8FINw3Fi9eKfcTQ_Zkw_PnPoy813ydy0iHrlotsrh1cdz5WdBCbe-R3akSWgjayca9X8Tzpv3o1rTDA; Hm_lpvt_3af9f141533380899e8c0acc32b1bcae=1722608540'

Headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "csrf-token": csrf_token,
    "isp-token": isp_token,
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "cookie": cookies,
    "Referer": "https://app.isellerpal.com/analysis/besetseller",
    "Referrer-Policy": "unsafe-url",
    "User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

DATA_RAW = {
  "currentPage": 1,
  "totalPage": 7732,
  "pageSize": 50,
  "total": 7732,
  "region": "it",
  "id": 46019,
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
