from typing import List

'''
 https://leetcode.com/problems/k-closest-points-to-origin/
 
 
'''


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points.sort(key=lambda point: (point[0]**2) + (point[1]**2))
        temp = list()
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            temp.append([[x, y], distance])

        temp.sort(key=lambda a: a[1])

        return list(map(lambda a: a[0], temp))[:k]
