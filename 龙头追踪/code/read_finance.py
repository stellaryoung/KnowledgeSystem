





#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import requests
from bs4 import BeautifulSoup

cookies = {
    'device_id': '24700f9f1986800ab4fcc880530dd0ed',
    's': 'c01beav5ud',
    'bid': '9cc36735295f03b7b249959fe26277bf_kef7rb57',
    'snbim_minify': 'true', 
    'remember': '1',
    'xq_a_token': 'e12fc0fabd00bf359d72a439a849d8eb144866f4', 
    'xq_id_token' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjQyMDMxMDYyMzcsImlzcyI6InVjIiwiZXhwIjoxNjE1MzAxNDA4LCJjdG0iOjE2MTI3MDk0MDgyMTgsImNpZCI6ImQ5ZDBuNEFadXAifQ.KQiYfhYtKDIplxPbFReY_CSl6W_JZJDnk1trs0a3oYzy_Z6LMu30fEgWor8qqJSsbtozZblJRLppsaip9QodRw5RJQGYlqrd1UAzHRbWCFRd7tvdfPEK0IKWrWO6bBX5xm65tJpzfwJepzS750vISuUGW9vJE_6FSfboLpzKq2Ozubq50Svo2bw3_oL0tyNWdVhGnizzMgthiALoP7Cy4zhFTyxEKTLZXMi5sXEGExflCzO6Lv6XHlB-8pUdXve0dhi99ebGeZfI1W7nRIEYJJbkXcHM4HgR_vEmA2H5xIC6yZxP9O0cYIG1zIuadcHhONLaFIOJ1aTUxRR1x1cHZw; xqat=e12fc0fabd00bf359d72a439a849d8eb144866f4',
    'xq_r_token': '0a526bf92721c67bece13f239a8dba07e1be3f91',
    'xq_is_login': '1',
    'u': '4203106237',
    'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1612026327,1612792769,1613480602,1613480610', 'is_overseas': '0',
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1614093638'
}


fake_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.2.1'
}

def request_url(url):
    response = requests.get(url, headers=fake_headers, cookies=cookies)
    return response.json()





if __name__ == "__main__":


    # https://stock.xueqiu.com/v5/stock/finance/cn/indicator.json?symbol=SH600036&type=Q4&is_detail=true&count=10&timestamp=
    res = {}
    with open('../raw/所有股票代码', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data = line.strip().split('\t')
            url = 'https://stock.xueqiu.com/v5/stock/finance/cn/indicator.json?symbol={}&type=Q4&is_detail=true&count=10&timestamp='.format(data[1])
            print(url)
            finance_data = request_url(url)
            if finance_data['error_code'] != 0:
                print(data)
                print('请求失败')
                time.sleep(5)
            res[data[0]] = finance_data
            time.sleep(0.1)
    
    with open('../raw/财务数据.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False)


    # url = 'https://stock.xueqiu.com/v5/stock/finance/cn/indicator.json?symbol=SH600036&type=Q4&is_detail=true&count=10&timestamp='
    # print(request_url(url))

