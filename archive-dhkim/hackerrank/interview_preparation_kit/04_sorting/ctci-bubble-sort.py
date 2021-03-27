# !/bin/python3

"""
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
"""

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(a):
    swap_cnt = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                swap_cnt += 1
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp

    print(f"Array is sorted in {swap_cnt} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
