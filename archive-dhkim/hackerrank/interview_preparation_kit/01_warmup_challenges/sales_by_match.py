#!/bin/python3

"""
https://www.hackerrank.com/challenges/sock-merchant/problem
"""

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    counter = dict()
    
    for a in ar:
        if a in counter:
            counter[a] += 1
        else:
            counter[a] = 1
            
    return sum([v//2 for v in counter.values()])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
