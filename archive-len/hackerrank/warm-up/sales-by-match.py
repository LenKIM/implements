#!/bin/python3
import collections
import os

# Complete the sockMerchant function below.
from math import floor
from typing import List


def sockMerchant(n: int, ar: List):
    if n == 1:
        return 0

    _dict = collections.defaultdict(int)

    for k in ar:
        _dict[k] = _dict[k] + 1

    result = 0
    for key, value in _dict.items():
        if value <= 1:
            continue
        f = floor(value / 2)
        result += f

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
