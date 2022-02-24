
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def request_url(url):
    response = requests.get(url)
    response = response.text

    return response

def parser_html(html):
    res = []
    soup = BeautifulSoup(html)
    soup = soup.find('table', id='NewStockTable')
    sub_soups = soup.find_all('tr')[2:]

    for sub_soup in sub_soups:
        data = sub_soup.find_all('div')
        code = data[0].text
        if not code.isdigit():
            continue
        # .encode('gbk').decode('utf-8', 'ignore')
        name = data[1].text
        # .encode('gbk').decode('utf-8', 'ignore')

        if code[:2] == '60':
            url = 'https://xueqiu.com/S/SH' + code
        else:
            url = 'https://xueqiu.com/S/SZ' + code

        res.append(code + '\t' + name + '\t' + url)

    return res

        




if __name__ == "__main__":
    res = []
    
    url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399673.phtml'
    html = request_url(url)
    data = parser_html(html)
    res.extend(data)
    res = list(set(res))
    res = '\n'.join(res)
    with open('../raw/创业板50.txt', 'w', encoding='utf-8') as f:
        f.write(res)

        
    