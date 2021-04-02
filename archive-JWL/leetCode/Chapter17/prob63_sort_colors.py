class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            while j > 0 and nums[j - 1] >= temp:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = temp
