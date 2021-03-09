#!/bin/python3

# https://www.hackerrank.com/challenges/strong-password/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def makePasswordStrong(n, password):
    changes = 0
    if not re.search('[0-9]', password):
        changes += 1
    if not re.search('[a-z]', password):
        changes += 1
    if not re.search('[A-Z]', password):
        changes += 1
    if not re.search(r'[!@#$%^&*()\-+]', password):
        changes += 1
    if (changes+n) < 6:
        changes += 6 - (changes+n)

    return changes

# Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 11

    password = "#HackerRank"

    answer = makePasswordStrong(n, password)

    # fptr.write(str(answer) + '\n')
    #
    # fptr.close()
