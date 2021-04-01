

if __name__ == "__main__":

    name2symbol = {}
    with open('../raw/所有股票代码', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data = line.strip().split('\t')
            name2symbol[data[0]] = data[1]
    res = []
    already = set()
    with open('../raw/龙头追踪', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data = line.strip().split()
            name = data[0]
            if name in already:
                continue
            already.add(name)
            symbol = name2symbol[name]
            url = 'https://xueqiu.com/S/' + symbol
            res.append(symbol + '\t' + name + '\t' + url + '\n')
    
    res = ''.join(res)
    with open('../龙头.txt', 'w', encoding='utf-8') as f:
        f.write(res)
