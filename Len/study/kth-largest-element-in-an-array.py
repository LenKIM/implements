import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freqs_heap = []
        result = 0
        aa = list()
        for num in nums:
            heapq.heappush(freqs_heap, -num)

        for _ in range(k):
            result = -heapq.heappop(freqs_heap)
            aa.append(result)

        return result

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


solution = Solution()
largest = solution.findKthLargest2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
print(largest)
