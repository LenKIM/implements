#!/bin/python3

"""
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
"""

import math
import os
import random
import re
import sys


# 각 원소를 모든 원소와 비교하여 절대편차를 구하는 O(n^2) 시간복잡도 방법
# def minimumAbsoluteDifference_naive(arr):
#     min_abs_diff = None
#     for i_idx, i_n in enumerate(arr):
#         for j_idx, j_n in enumerate(arr):
#             if i_idx == j_idx:
#                 continue
#
#             abs_diff = abs(i_n - j_n)
#             if min_abs_diff is None:
#                 min_abs_diff = abs_diff
#             else:
#                 min_abs_diff = min(min_abs_diff, abs_diff)
#
#     return min_abs_diff


def minimumAbsoluteDifference_sort(arr):
    def quick_sort(nums):

        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]
        smaller_sub, equal_sub, bigger_sub = [], [], []
        for n in nums:
            if n < pivot:
                smaller_sub.append(n)
            elif n > pivot:
                bigger_sub.append(n)
            else:
                equal_sub.append(n)

        left_sub = quick_sort(smaller_sub)
        right_sub = quick_sort(bigger_sub)

        return left_sub + equal_sub + right_sub

    sorted_arr = quick_sort(arr)

    min_abs_diff = None

    for idx in range(len(sorted_arr) - 1):
        diff = abs(sorted_arr[idx] - sorted_arr[idx+1])
        if min_abs_diff is None:
            min_abs_diff = diff
        else:
            min_abs_diff = min(min_abs_diff, diff)

    return min_abs_diff


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     result = minimumAbsoluteDifference(arr)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
