#!/bin/python

import math
import os
import random
import re
import sys




S = raw_input()
try:
    a = int(S)
    print(a)
except ValueError:
    print("Bad String")