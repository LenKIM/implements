import collections
import sys
from typing import List

"""
https://leetcode.com/problems/sliding-window-maximum/

배열 nums가 주어졌을 때 k크기의 슬라이딩 원도우를 오른쪽 끝까지 이동하면서 최대 슬라이딩 원도우를 구하라.

nums = [1,3,-1,-3,5,3,6,7], k = 3

문제를 풀기 위해서?

깔끔하게 값을 제거 

"""


class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if not nums:
    #         return nums
    #
    #     list = []
    #     for i in range(len(nums) - k + 1):
    #         list.append(max(nums[i:i + k]))
    #
    #     return list
    # nums = [1,3,-1,-3,5,3,6,7], k = 3
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = collections.deque()
        res = []
        for idx, val in enumerate(nums):

            if q and idx - q[0] == k:
                q.popleft()

            # 완전 제거
            while q and nums[q[-1]] <= nums[idx]:
                q.pop()

            q.append(idx)

            if idx + 1 >= k:
                res.append(nums[q[0]])
        return res



# max를 계산하지 말아야해...
window = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(window)
