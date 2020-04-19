try:
    n= int(input())
    code=0
    total=[]
    for _ in range(n):
        a,b,c = map(int,input().split())
        code +=a
        total.append([b+c,a])
    total.sort()
    ans = -1
    i=0
    while i<n and ans < code+total[i][0]:
        ans = code + total[i][0]
        code -= total[i][1]
        i+=1
    print(ans)
    
except:
    pass
