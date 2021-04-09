
class Solution:
    def search_nums(self, nums: List[int], target, start, end)->int:
        mid: int = (start + end) // 2
        res: int = -1
        if start<=end:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return self.search_nums(nums, target, mid+1, end)
            elif target < nums[mid]:
                return self.search_nums(nums, target, start, mid-1)
        return res

    def search(self, nums: List[int], target: int) -> int:
        return self.search_nums(nums, target, 0, len(nums)-1)
