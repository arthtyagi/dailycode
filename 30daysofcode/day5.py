#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    result=0
    for i in range(1,11):
        result=n*i
        print (f"{n} x {i} = {result}")
        i+=1
