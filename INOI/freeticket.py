## FIRST PROBLEM ON THE INOI PRACTICE SECTION

try:
    cities,flights=list((map(int,input().split())))
    arr = [[float("inf") for i in range(cities+1)] for j in range(cities+1)]
    for i in range(flights):
        c1,c2,price = list((map(int,input().split())))
        arr[c1][c2]= price
        arr[c2][c1]= price

    ## since the price for traveling to the same city would be practically none
    for i in range(1,cities+1):
        arr[i][i]=0
    
    for i in range(1,cities+1):
        for j in range(1,cities+1):
            for k in range(1,cities+1):
                arr[j][k]= min(arr[j][k], arr[j][i]+arr[i][k]) ## the arr[j][k] is inf if there is no route hence we have the second param which finds an alternative route
    
    minumum = float("-inf")
    for i in range(1,cities+1):
        for j in range(1,cities+1):
            if i!=j:
                minimum = max(minimum,arr[i][j])
    print (minimum)
except:
    pass
