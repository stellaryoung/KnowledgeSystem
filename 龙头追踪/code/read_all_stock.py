

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


fake_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.2.1'
}

def request_url(url):
    response = requests.get(url, headers=fake_headers)
    return response.json()





if __name__ == "__main__":
    already = set()
    with open('../龙头追踪', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data = line.strip().split()
            already.add(data[0])

    url = 'https://xueqiu.com/service/screener/screen?category=CN&exchange=sh_sz&areacode=&indcode=&order_by=symbol&order=desc&page=1&size=30&only_count=0&current=&pct=&mc=&volume=&_=1610280710755'
    data = request_url(url)
    all_num = str(data['data']['count'])

    new_url = 'https://xueqiu.com/service/screener/screen?category=CN&exchange=sh_sz&areacode=&indcode=&order_by=symbol&order=desc&page=1&size={}&only_count=0&current=&pct=&mc=&volume=&_=1610280710755'.format(all_num)

    res = []
    dataes = request_url(new_url)
    for data in dataes['data']['list']:
        name = data['name']
        symbol = data['symbol']
        if 'ST' in name:
            continue
        # if name in already:
        #     continue
        res.append(name + '\t' + symbol)

    print(len(res))
    res = '\n'.join(res)
    with open('所有股票代码', 'w', encoding='utf-8') as f:
        f.write(res)



