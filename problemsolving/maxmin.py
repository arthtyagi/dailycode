import collections, sys
if __name__=='__main__':
    n= int(sys.stdin.readline())
    k=int (sys.stdin.readline())
    x= sorted(int(sys.stdin.readline()) for _ in range(n))
    print(min(x[i+k-1]-x[i] for i in range(0, n-k-1)))
