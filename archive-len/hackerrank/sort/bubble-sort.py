#!/bin/python3

# Complete the countSwaps function below.
from typing import List


def countSwaps(a: List):
    a_len = len(a)
    swap_count = 0

    for i in range(a_len):
        for j in range(a_len-1):
            if a[j] > a[j+1]:
                swap_count = swap_count + 1
                a[j], a[j+1] = a[j+1], a[j]

    print(f'Array is sorted in {swap_count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')


if __name__ == '__main__':
    # n = int(input())

    # a = list(map(int, input().rstrip().split()))

    countSwaps([4,2,3,1])
