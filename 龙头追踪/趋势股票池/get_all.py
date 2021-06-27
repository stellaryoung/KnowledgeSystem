

stock2code = {}

with open('股票代码', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        data = line.strip().split()
        stock2code[data[0]] = data[1]

res = []
with open('趋势选股', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        data = line.strip().split()
        stock = data[0]
        code = stock2code[stock]

        res.append([stock, code])

res = sorted(res, key=lambda x: int(x[1][2:]))
res = [key + '\t'+ val for key, val in res]

res = '\n'.join(res)
with open('趋势股票池', 'w', encoding='utf-8') as f:
    f.write(res)
