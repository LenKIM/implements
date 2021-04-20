from functools import cmp_to_key
from typing import List


def compare(x, y):
    x_res = x[0]**2 + x[1]**2
    y_res = y[0]**2 + y[1]**2
    if x_res<y_res:
        return -1
    elif x_res==y_res:
        return 0
    else:
        return +1

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = sorted(points, key=cmp_to_key(compare))
        return res[:k]
