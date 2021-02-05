from typing import List

"""
https://leetcode.com/problems/product-of-array-except-self
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1 for _ in range(len(nums))]

        prod_left = 1
        for idx, n in enumerate(nums[:-1]):
            prod_left *= n
            res[idx + 1] *= prod_left

        prod_right = 1
        for idx, n in enumerate(nums[:0:-1]):
            prod_right *= n
            res[len(res) - idx - 2] *= prod_right

        return res

