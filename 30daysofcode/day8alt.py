##30.00 POINTS USING THIS SOLUTION, ADDED TRY AND EXCEPT

n = int(input().strip())
phone_book={}
for i in range(n):
    x= input().strip()
    listx = list(x.split(' '))
    phone_book[listx[0]] = listx[1]
name=[]
try:
    while True:
        inp = input().strip()
        if inp != "":
            name.append(inp)
        else:
            break
except EOFError:
    pass
for i in name: 
    if i in phone_book:
        print(i+'='+phone_book[i])
    else:
        print('Not found')
