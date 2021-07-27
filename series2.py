import math
import numpy as np



# intervals for all series members,

x = np.arange(2,11,1)
xx = np.arange(2,101,1)
xxx = np.arange(2,1001,1)
xxxx = np.arange(2,10001,1)
xxxxx = np.arange(2,100001,1)
xxxxxx = np.arange(2,1000001,1)
xxxxxxx = np.arange(2,10000001,1)
#write series please a_n term in >>>a<<<

series = lambda i:1/(i)
def f(a):
    w=[]
    for i in a:
        w.append(series(i))
        length = len(w)
    #print(w)
    s = 0
    for number in w:
        s = s + number
    
    return s

first = f(x)
second = f(xx)
third = f(xxx)
four = f(xxxx)
five = f(xxxxx)
six = f(xxxxxx)
print(first,second,third,four,five,six)
print(second-first,third-second,four-third,five-four,six-five)
