class Solution(object):

    def search(self, nums, target):
        if not nums:
            return -1

        # 최솟값 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        # 최소값
        pivot = left
# 0 이라는 값을 가진 4번쨰 idx
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2 # 일반적으로는 얘가 Pivot
            mid_pivot = (mid + pivot) % len(nums) # 중앙값, 로테이션 돌린 만큼 더해주기.

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1

search = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
# search = Solution().search([0, 1, 2, 4, 5, 6, 7], 0)
print(search)
