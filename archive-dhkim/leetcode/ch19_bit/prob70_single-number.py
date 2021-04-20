from typing import List

"""
https://leetcode.com/problems/single-number/
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n

        return res
