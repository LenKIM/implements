#!/bin/python3

"""
https://www.hackerrank.com/challenges/repeated-string/problem
"""

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_cnt = len([c for c in s if c == 'a'])
    epoch = n // len(s)
    epoch_a_cnt =  a_cnt * epoch
    
    least = n % len(s)
    least_a_cnt = len([c for c in s[:least] if c == 'a'])
    
    return epoch_a_cnt + least_a_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
