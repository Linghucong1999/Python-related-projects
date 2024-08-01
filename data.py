import os


URL = 'https://app.isellerpal.com/api-product/best-seller-1000-list'
METHOD = 'POST'

Cookie = 'guestId=b6338646d7d54633a479eeb69982ce99; Hm_lvt_282b3ee77c50ff5447b7b85d121a397d=1722082749; Hm_lvt_3af9f141533380899e8c0acc32b1bcae=1722002528,1722349973; HMACCOUNT=936E517E1196FE4B; token=eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOjE2MTIxNywic3ViIjoiMTYxMjE3IiwiaWF0IjoxNzIyMzQ5OTk1LCJleHAiOjE3MjI5NTQ3OTV9.bVuD341t5WRBY3pD0iTyyq63eqVIddDp-LLgqTk69trPerbJyN_Wu3VmVIIqWSN8vpi7R4p9rLkQIdhVkVMXbw; Hm_lpvt_3af9f141533380899e8c0acc32b1bcae=1722528993'

isp_token='eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOjE2MTIxNywic3ViIjoiMTYxMjE3IiwiaWF0IjoxNzIyMzQ5OTk1LCJleHAiOjE3MjI5NTQ3OTV9.bVuD341t5WRBY3pD0iTyyq63eqVIddDp-LLgqTk69trPerbJyN_Wu3VmVIIqWSN8vpi7R4p9rLkQIdhVkVMXbw'

csrf_token = os.popen('node ./index.js').read().strip()
print(csrf_token)
Headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "csrf-token": 'TSVCVm2XrPKbvV4OKgwCKCMSFi/8rPa4jekzYLafypc=',
    "isp-token": isp_token,
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
