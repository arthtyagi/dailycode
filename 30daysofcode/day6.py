import os
import math

def solve(S):
    e,o=S[::2],S[1::2]
    print(e+' '+o)

if __name__ =='__main__':
    T= int(input().strip())
    for i in range(T):
        S=input()
        solve(S)
        
