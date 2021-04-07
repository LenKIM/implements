class Solution(object):
    def search(self, nums, target):
        l, r = 0 , len(nums)-1
        while l<=r :
            mid = (l+r)//2
            if nums[mid]== target:
                return mid
            elif nums[l] <= nums[mid] :
                if nums[mid] < target or (nums[mid] > target and nums[l] > target):
                    l = mid+1
                else :
                    r = mid-1
            else :
                if nums[mid] > target or(nums[mid] < target and nums[r] < target):
                    r = mid-1
                else :
                    l = mid +1
        return -1
