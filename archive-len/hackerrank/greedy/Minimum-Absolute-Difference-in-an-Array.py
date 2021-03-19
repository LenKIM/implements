#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
from typing import List


# TODO 다르게 풀 수 있을 것 같음. 이런 정답 말고, 이야기해봅시다.

def minimumAbsoluteDifference(arr: List):
    arr.sort()

    append = arr[1:]
    behind = arr[:-1]
    mx = sys.maxsize
    for i, j in zip(append, behind):
        mx = min(mx, i - j)

    return mx


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    arr = list([3, 4, 1, 4])

    result = minimumAbsoluteDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
