#!/bin/python3

import math
import os
import random
import re
import sys

def solve(k):
    if k%2!=0:
        print("Weird")
    if k%2==0: 
        if k>=6 and k<=20: print("Weird")
        else: print("Not Weird")

if __name__ == '__main__':
    N = int(input())
    solve(N)
