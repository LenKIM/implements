from typing import List

"""
https://leetcode.com/problems/intersection-of-two-arrays/
"""


class Solution01:
    """
    교집합 찾기 (1) - 해쉬셋을 이용한 풀이
    Runtime : 40 ms
    Memory : 14.3 MB
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.intersection(set2))


class Solution02:
    """
    교집합 찾기 (2) - 이진검색을 이용한 풀이
    Runtime : 52 ms
    Memory : 14.6 MB
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def binary_search(ary: List[int], target: int):

            if len(ary) < 1:
                return False

            middle_idx = len(ary) // 2

            if ary[middle_idx] < target:
                return binary_search(ary[middle_idx+1:], target)
            elif ary[middle_idx] > target:
                return binary_search(ary[:middle_idx], target)
            else:
                return True

        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))

        intersection_list = []
        for n in nums1:
            if binary_search(nums2, n):
                intersection_list.append(n)

        return intersection_list
