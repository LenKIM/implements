#!/bin/python3

import os


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):

    results = 0
    level = 0
    for p in range(steps):
        if path[p] == 'U':
            level += 1
        else:
            if level == 0:
                results += 1

            level = level - 1
    return results


# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
