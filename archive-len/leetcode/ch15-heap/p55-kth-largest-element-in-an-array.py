import heapq
from typing import List


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heap = list()
    #     for n in nums:
    #         heapq.heappush(heap, -n)
    #
    #     heappop = 0
    #     for _ in range(k):
    #         heappop = heapq.heappop(heap)
    #
    #     return -heappop

    # heapq 모듈의 heapify 이용

    ##
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heapq.heapify(nums)
    #
    #     for _ in range(len(nums) - k):
    #         heapq.heappop(nums)
    #
    #     return heapq.heappop(nums)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


solution = Solution()
largest = solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(largest)
