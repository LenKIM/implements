class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        res = -1
        for i in range(len(nums)):
            if nums[i] == target:
                res = i
                break
        return res;






