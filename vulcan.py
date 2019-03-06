# -*- coding:utf-8 -*-
import random
data = [random.randint(1,100) for i in range(10)]
print(data)
for i in range(len(data)):
    for j in range(len(data)-1-i):
        if data[j]>data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]
            pass
print(data)
