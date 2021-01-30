#!/bin/python3

# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

# 3
# {[()]}
# {[(])}
# {{[[(())]]}}

# YES
# NO
# YES


# Complete the isBalanced function below.
import os


def isBalanced(s):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for c in s:
        if c not in table:
            stack.append(c)
        elif not stack or table[c] != stack.pop():
            return "NO"

    # return len(stack) == 0
    return "YES" if len(stack) == 0 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        fptr.write(result + '\n')

    fptr.close()
