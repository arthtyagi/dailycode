n, k = map(int, input().strip().split())

luck = 0
important = []

for i in range(n): 
    l,t = list(map(int, input().strip().split()))
    if t == 0:
        luck+=l
    else:
        important.append(l)
for i in sorted(important, reverse= True):
    if k>0:
        luck += i
        k -= 1
    else: 
        luck -= i
print(luck)
