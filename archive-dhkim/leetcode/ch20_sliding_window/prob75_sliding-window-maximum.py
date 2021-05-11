import collections
from typing import List

"""
https://leetcode.com/problems/sliding-window-maximum/submissions/
"""


class Solution:
    """
    이 문제는 본 답안처럼 풀어도 타임아웃이 난다.
    max() 자체를 사용하지 않는 방법으로 다시 풀어볼 것
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        # window = []
        window = collections.deque()
        local_max = float('-inf')

        for idx, v in enumerate(nums):
            window.append(v)
            # if len(window) < k:
            if idx < k - 1:
                continue

            if local_max == float('-inf'):
                local_max = max(window)
            elif local_max < v:
                local_max = v

            max_list.append(local_max)

            # if window.pop(0) == local_max:
            if window.popleft() == local_max:
                local_max = float('-inf')

        return max_list
