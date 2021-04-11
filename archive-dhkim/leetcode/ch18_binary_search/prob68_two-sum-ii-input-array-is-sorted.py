from typing import List

"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarysearch(gte_idx, lte_idx, t_val):
            if gte_idx <= lte_idx:
                mid_idx = (gte_idx + lte_idx) // 2
                mid_val = numbers[mid_idx]

                if t_val < mid_val:
                    return binarysearch(gte_idx, mid_idx - 1, t_val)
                elif t_val > mid_val:
                    return binarysearch(mid_idx + 1, lte_idx, t_val)
                else:
                    return mid_idx
            else:
                return -1

        for idx, n in enumerate(numbers):
            least = target - n

            res_idx = binarysearch(0, len(numbers) - 1, least)

            if res_idx != idx and res_idx != -1:
                return sorted([idx + 1, res_idx + 1])

        return [-1, -1]
