import collections
from typing import List
'''
https://leetcode.com/problems/single-number/

한 개 빼고 두번씩 보여준다. 빠진 한 개 찾기

Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
'''
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     q = []
    #     for num in nums:
    #         if q.__contains__(num):
    #             q.remove(num)
    #         else:
    #             q.append(num)
    #
    #     if len(q) == 1:
    #         return q[0]

    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num

        return answer


number = Solution().singleNumber([2, 2, 1])
print(number)
