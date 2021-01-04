#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    final = list(collections.Counter(ar).values())
    finalsum = 0
    for i in range(len(final)):
        if (final[i] >= 2):
            if (final[i] % 2) is 0:
                finalsum += final[i]
            else:
                finalsum += (final[i]-1)
    return (finalsum // 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
