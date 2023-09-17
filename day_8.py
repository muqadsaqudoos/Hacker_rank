n= int(input())
dictt = {}
for i in range(n):
    text = input().split()
    dictt[text[0]] = text[1]
    
while(True):
    try:
        query = input()
        if query in dictt:
            print(query+"="+dictt[query])
        else:
            print('Not found')
    except EOFError:
        break
