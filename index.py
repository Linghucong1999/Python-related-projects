import requests
import math
from data import URL, METHOD, Headers, DATA_RAW
import pandas as pd
import time

asin_storage = []


def requests_post(method, url, headers, data):
    session = requests.Session()
    return session.request(method=method, url=url, headers=headers, json=data)


# 清洗数据

def clean_data(data):
    list_data = data['result']
    return [(item['asin'], item['brandName']) for item in list_data['list'] if "price" not in item]


if __name__ == "__main__":
    data = requests_post(METHOD, URL, Headers, DATA_RAW).json()
    if data['code'] != 0:
        print('result not in data', data)
        exit()
    result = data['result']
    total = result['total']
    pageSize = result['pageSize']
    totalPage = math.ceil(total / pageSize)
    for i in range(1, totalPage + 1):
        DATA_RAW['currentPage'] = i
        data = requests_post(METHOD, URL, Headers, DATA_RAW).json()
        if 'result' not in data:
            print('result not in data', data)
            continue
        asin = clean_data(data)
        asin_storage.extend(asin)
        time.sleep(2)
    df = pd.DataFrame(asin_storage, columns=['ASIN', 'BrandName'])
    ground = df.groupby('BrandName')['ASIN'].apply(list).reset_index()
    excel_path = 'asin.xlsx'
    ground.to_excel(excel_path, index=False)
