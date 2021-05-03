#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    cnt = 0
    for i in range(n):
        for j in range(n-1):
            if(a[j]> a[j+1]) :
                a[j], a[j+1] = a[j+1], a[j]
                cnt+=1

    print("Array is sorted in" ,cnt , "swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
