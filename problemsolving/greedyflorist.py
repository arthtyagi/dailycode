n,k = [int(i) for i in input().split(" ")]
cost = [-int(i) for i in input().split(" ")]
cost = sorted(cost)
total =0
for i in range(n):
    total -= cost[i]*(i//k+1)
print(total)
