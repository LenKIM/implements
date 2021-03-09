#!/bin/python3

# https://www.hackerrank.com/challenges/reduced-string/problem
import collections
import os


# Complete the superReducedString function below.
def superReducedString(s):
    res = []

    for c in s:
        if res and c == res[-1]:
            res.pop()
        else:
            res.append(c)
    return "".join(res)

def super_reduced_string(s, i):
    if i < 0:
        i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            return super_reduced_string(s[:i] + s[i+2:], i-1)
        i += 1
    return s

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "aaabccddd"

    result = super_reduced_string(s, 0)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
