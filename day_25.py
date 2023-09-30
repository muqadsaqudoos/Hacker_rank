# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from math import sqrt 

def prime_number(num):
    for i in range(2,int(sqrt(num))+1):
        if num%i ==0 :
            return False
    return True
    
n = int(input())
for i in range(n):
    a = int(input())
    if a>=2 and prime_number(a):
        print("Prime")
    else:
        print("Not prime")