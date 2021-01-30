from typing import List

"""
https://leetcode.com/problems/array-partition-i
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)

        return sum([min(n, nums[idx + 1]) for idx, n in enumerate(nums) if idx % 2 == 0])
