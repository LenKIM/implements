#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s="abc", n=10):

    #abc_list = "".join(["abc"] * 7)
    #abc_string = abc_list[:10]

    #"abc abc abc abc abc abc abc ..."
    # 10 개

    a_len = len(s)

    a_mod_n = n / a_len
    mock = math.floor(a_mod_n)

    rest = n % a_len

    contains_a_in_s = 0
    for c in s:
        if c == "a":
            contains_a_in_s += 1

    contains_a_in_s_count = (contains_a_in_s * mock)

    rest = s[:rest]

    for c in rest:
        if c == "a":
            contains_a_in_s_count += 1

    return contains_a_in_s_count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
