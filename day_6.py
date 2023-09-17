# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0,n):
    s = input()
    l = len(s)
    j=0
    while(j<=(l-1)):
        print(f'{s[j]}',end='')
        j = j+2
    print(end=' ')
    j=1
    while(j<=(l-1)):
        print(f'{s[j]}',end='')
        j = j+2
    print()
        
    
