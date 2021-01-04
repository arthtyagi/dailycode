#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    l = len(c)-1
    i = 0
    while i < l:
        if c[i] is 0 and c[i+1] is 0:
            if i<=(l-2) and c[i+2] is 0:
                jumps += 1
                i += 2
            else :
                jumps += 1
                i += 1
        elif c[i] is 0 and c[i+1] is 1:
            jumps += 1
            i += 2
            
    return (jumps)            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
