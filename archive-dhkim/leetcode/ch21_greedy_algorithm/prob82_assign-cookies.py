from typing import List

"""
https://leetcode.com/problems/assign-cookies
"""


class Solution:
    """
    runtime: 172 ms
    memory: 16.2 MB
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res_tuples = []

        for each_s in s:
            if g and g[0] <= each_s:
                res_tuples.append((each_s, g.pop(0)))

        return len(res_tuples)
