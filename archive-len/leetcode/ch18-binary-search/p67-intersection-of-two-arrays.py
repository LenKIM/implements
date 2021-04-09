import bisect
from typing import List

'''
https://leetcode.com/problems/intersection-of-two-arrays/
두 배열의 교집합
[1,2,2,1]
[2,2]
= [ 2 ]

[4,9,5]
[9,4,9,8,4]
= [9,4]
'''


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()

        for n1 in nums1:
            index = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and \
                    len(nums2) > index and \
                    n1 == nums2[index]:
                result.add(n1)

        return result
