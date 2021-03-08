#!/bin/python3

# https://www.hackerrank.com/challenges/camelcase/problem
# https://www.martinkysel.com/hackerrank-camelcase-solution/
import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    res = []
    a:str = "1"
    a.isupper()
    current_idx = 0
    for idx, c in enumerate(s):
        if c.isupper():
            idx_ = s[current_idx: idx]
            current_idx = idx
            res.append(idx_)


    return len(res) + 1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "oneTwoThree"
    s = "asdasdasd"

    result = camelcase(s)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
