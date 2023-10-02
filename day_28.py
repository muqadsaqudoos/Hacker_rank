#!/bin/python3

import math
import os
import random
import re
import sys

a = "@gmail.com"
namelist = []
if __name__ == '__main__':
    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if a in emailID:
            namelist.append(firstName)
        namelist.sort()
    for i in namelist:
        print(i)
