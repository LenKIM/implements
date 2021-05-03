from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res:List[int] = []
        nums1.sort()
        nums2.sort()

        for num1 in nums1:
            l, r = 0, len(nums2)-1
            while l<=r:
                mid = (l+r)//2
                if nums2[mid] < num1:
                    l = mid+1
                elif nums2[mid]>num1:
                    r = mid-1
                else :
                    if num1 not in res:
                        res.append(num1)
                    break
        return res