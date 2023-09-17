#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
a = n
start = n
b = []
d = []
e = 0
while(n!=0):
    a = n%2
    n = n//2
    b.append(a)
b.reverse()    
c = list(map(str, b))
str = ("")
for i in range(len(c)):
    str= str+c[i]
for i in range(len(b)):
    if b[i] == 1:
        e = e+1
    else:
        d.append(e)
        e=0
d.append(e)
print(max(d))
    

