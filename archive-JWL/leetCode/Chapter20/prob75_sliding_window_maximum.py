from typing import List, Collection


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = end = left = 0
        need = Collection.Counter(t)
