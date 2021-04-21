class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n - k + 1):
            res.append(max(nums[i:i+k]))
        return res