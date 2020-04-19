#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    a = []
    for _ in range(6):
        a.append(list(map(int, input().rstrip().split())))

    sumslist=[]
    for j in range(0,4):
        for i in range(0,4):
            sum=(a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1]+ a[i+2][j+2])
            sumslist.append(sum)
    print(max(sumslist))
