#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/13 16:54
# @Author : Patrick
# @File : test.py
# @Software: PyCharm

l = ['Cars', 'Canary', 'Carpet', 'Cartoon', 'Carbon', 'Carpool', 'Carpenter', 'Cartel', 'Carton', 'Caravan', 'Cartop']
idx = 0
k = 0
while k < 9:
    a = []
    for i in l:
        if idx < len(i) and i[idx] not in a:
            a.append(i[idx])
    print(a)
    idx += 1
    k += 1
