#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
i=-1
a = -n
while(i >= a):
    print(arr[i],end=' ')
    i = i-1
