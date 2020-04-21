#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

def solve(N):
    count= 0
    maxcount = 0
    for i in str(bin(N)):
        if i == '1':
            count +=1
        elif count > maxcount:
            maxcount = count;
            count = 0
        else:
            count = 0
    if count > maxcount: maxcount = count        
    return(maxcount)   
if __name__ == '__main__':
    N = int(input())
    print(solve(N))


## TRY THIS USING ITERTOOLS AS WELL
