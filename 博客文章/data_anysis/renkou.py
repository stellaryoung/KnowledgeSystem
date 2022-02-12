

import matplotlib.pyplot as plt
# https://www.bilibili.com/read/cv4779911/

renkou = []
with open('./china', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        data = line.strip().split('：')
        renkou.append(int(data[1]))

x = range(0, len(renkou))

x_tricks = [1940 + 5 * i for i in range(16)]
plt.figure(figsize=(10, 6))
plt.plot(x,renkou,'')  

plt.show()