from typing import List

"""
https://leetcode.com/problems/top-k-frequent-elements
"""


class Solution01:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        return [k for k, v in Counter(nums).most_common(k)]
