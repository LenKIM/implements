#!/bin/python3

"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    edge_list = []
    skip_cloud = False
    for cloud in c[1:]:
        if cloud == 1:
            skip_cloud = True
        else:
            if skip_cloud:
                edge_list.append(2)
                skip_cloud = False
            else:                
                if len(edge_list) > 0 and edge_list[-1] == 1:
                    edge_list[-1] = 2
                else:
                    edge_list.append(1)
            
    return len(edge_list)    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
