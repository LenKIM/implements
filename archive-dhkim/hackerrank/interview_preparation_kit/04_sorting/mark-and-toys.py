#!/bin/python3

"""
https://www.hackerrank.com/challenges/mark-and-toys/problem
"""

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    def quickSort(nums):
        if len(nums) <= 1:
            return nums

        pivot_idx = len(nums) // 2
        pivot = nums[pivot_idx]

        left_sub = quickSort([n for n in nums if n < pivot])
        middle_sub = [n for n in nums if n == pivot]
        right_sub = quickSort([n for n in nums if n > pivot])

        return left_sub + middle_sub + right_sub

    sorted_prices = quickSort(prices)

    price_sum = 0
    toy_cnt = 0

    for price in sorted_prices:
        if price_sum + price < k:
            price_sum += price
            toy_cnt += 1
        else:
            break

    return toy_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
