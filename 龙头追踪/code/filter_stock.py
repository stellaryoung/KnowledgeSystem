





if __name__ == "__main__":
    already = set()
    with open('../raw/龙头追踪', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data = line.strip().split()
            already.add(data[0])
    
    res = []
    with open('所有股票代码', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data = line.strip().split('\t')
            if data[0] in already:
                continue
            res.append(line)
    
    res = ''.join(res)
    with open('raw_roe20', 'w', encoding='utf-8') as f:
        f.write(res)

