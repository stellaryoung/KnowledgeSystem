
#! /usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    filename = '../沪深300.txt'
    
    with open(filename, 'r', encoding='utf-8') as f:
        dataes = f.readlines()
        dataes = set(dataes)
        # print(len(dataes))
        # for line in dataes:
        #     data = line.strip().split('\t')
        #     code = data[0]
        #     name = data[1]
        #     url = data[2]
        #     if '银行' in name or '证券' in name:
        #         continue

    print(len(dataes))
    dataes = ''.join(dataes)
    with open('res', 'w', encoding='utf-8') as f:
        f.write(dataes)

