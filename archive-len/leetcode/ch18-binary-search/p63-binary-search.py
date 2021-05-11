from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def dfs(_nums, _target, low=None, high=None):
            low, high = low or 0, high or len(nums) - 1

            if low > high:
                return -1
            mid = (low + high) // 2

            if nums[mid] > target:
                return dfs(nums, target, low, mid)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return dfs(nums, target, mid + 1, high)

        return dfs(nums, target)


search = Solution().search([-1, 0, 3, 5, 9, 12], 9)
print(search)
