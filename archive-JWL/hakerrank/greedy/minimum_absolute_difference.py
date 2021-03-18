#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# 첫 풀이 방
#def subtract(x):
#    res = x[0] - x[1]
#    return res if res>0 else -res
#def minimumAbsoluteDifference(arr):
#    lis = list(map(subtract,itertools.combinations(arr,2)))
#    return min(lis)

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    min_no = sys.maxsize
    for i in range(0, len(arr)-1):
        sub = arr[i+1] - arr[i]
        min_no = sub if min_no > sub else min_no
    return min_no

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
