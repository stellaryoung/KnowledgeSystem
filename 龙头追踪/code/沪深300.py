
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

        if code[:3] == '600':
            url = 'https://xueqiu.com/S/SH' + code
        else:
            url = 'https://xueqiu.com/S/SZ' + code

        res.append(code + '\t' + name + '\t' + url)

    return res

        




if __name__ == "__main__":
    res = []
    for i in range(1, 9):
        # http://vip.stock.finance.sina.com.cn/corp/view/vII_NewestComponent.php?page=2&indexid=000300
        url = 'http://vip.stock.finance.sina.com.cn/corp/view/vII_NewestComponent.php?page={}&indexid=000300'.format(str(i))
    
        html = request_url(url)
        data = parser_html(html)
        res.extend(data)
    print(len(res))
    res = list(set(res))
    print(len(res))
    res = '\n'.join(res)
    with open('../raw/沪深300.txt', 'w', encoding='utf-8') as f:
        f.write(res)

        
    