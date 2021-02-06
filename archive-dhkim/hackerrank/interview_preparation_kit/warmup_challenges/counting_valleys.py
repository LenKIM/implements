#!/bin/python3

"""
https://www.hackerrank.com/challenges/counting-valleys/problem
"""

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys_cnt = 0    
    height = 0
    for idx, p in enumerate(path):
        unit = {'D': -1, 'U': 1}.get(p)
        if idx > 0 and height < 0 and height + unit == 0:
            valleys_cnt += 1        
        height += unit
        
    return valleys_cnt
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
