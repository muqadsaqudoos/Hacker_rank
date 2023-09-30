# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def prime_number(num):
    if num<=1:
        return False
    elif num ==2:
        return True
    elif num%2 == 0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i ==0 :
            return False
    return True
    
n = int(input())
for i in range(n):
    a = int(input())
    if prime_number(a):
        print("Prime")
    else:
        print("Not prime")