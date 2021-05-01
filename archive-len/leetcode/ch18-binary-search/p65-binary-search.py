import bisect
from typing import List


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #
    #     def dfs(_nums, _target, low=None, high=None):
    #         low = low or 0
    #         if high is None:
    #             high = len(_nums) - 1
    #
    #         if low > high:
    #             return -1
    #         mid = (low + high) // 2
    #
    #         if _nums[mid] > target:
    #             return dfs(_nums, target, low, mid - 1)
    #         if _nums[mid] == target:
    #             return mid
    #         if _nums[mid] < target:
    #             return dfs(_nums, target, mid + 1, high)
    #
    #     return dfs(nums, target)

    # def search(self, nums: List[int], target: int) -> int:
    #
    #     def bs(left, right):
    #         if left <= right:
    #             mid = (left + right) // 2
    #
    #             if nums[mid] < target:
    #                 return bs(mid+1, right)
    #             elif nums[mid] > target:
    #                 return bs(left, mid-1)
    #             else:
    #                 return mid
    #         else:
    #             return -1
    #     return bs(0, len(nums)-1)
    #
    # def search(self, nums: List[int], target: int) -> int:
    #     left,right = 0, len(nums) -1
    #
    #     while left <= right:
    #         mid = (left + right) // 2
    #
    #         if nums[mid] < target:
    #             left = mid + 1
    #
    #         elif nums[mid] > target:
    #             right = mid - 1
    #         else:
    #             return mid
    #     return -1

    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


search = Solution().search([-1, 0, 3, 5, 9, 12], 9)
print(search)
