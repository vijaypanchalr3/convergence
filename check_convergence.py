# -*- coding: utf-8 -*-
import math
import numpy as np



# intervals for all series members,

x = np.arange(1,11,1)
xx = np.arange(1,101,1)
xxx = np.arange(1,1001,1)
xxxx = np.arange(1,10001,1)
xxxxx = np.arange(1,100001,1)
xxxxxx = np.arange(1,1000001,1)
xxxxxxx = np.arange(1,10000001,1)

# write a_n th term in 'i'
series = lambda i:1/(i**2)
def f(a):
    w=[]
    for i in a:
        w.append(series(i))
        length = len(w)
    #print(w)
    s = 0
    for number in w:
        s = s + number
    return print('from 1 to',length,'integers series summation is ',s)

# some series are very divergence, so start with less f's and delete f(xxxx),f(xxxxx), f(xxxxxx)
f(x)
f(xx)
f(xxx)
f(xxxx)
f(xxxxx)
f(xxxxxx)
