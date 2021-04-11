from typing import List

"""
https://leetcode.com/problems/binary-search/submissions/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recur(i, j):
            if i <= j:
                middle_idx = (i + j) // 2
                if nums[middle_idx] == target:
                    return middle_idx
                elif nums[middle_idx] > target:
                    return recur(i, middle_idx - 1)
                else:
                    return recur(middle_idx + 1, j)
            else:
                return -1

        return recur(0, len(nums) - 1)
