#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    s= [str(arr) for arr in arr]
    print (" ".join(s[::-1]))
