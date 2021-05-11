"""
https://leetcode.com/problems/hamming-distance
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum([int(a) for a in bin(x ^ y)[2:]])
