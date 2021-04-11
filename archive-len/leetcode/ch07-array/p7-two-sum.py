from typing import List


# [2, 7, 11, 15]
#  target > 9 라면? 2, 7을 더해야 함. 그 때 인덱스를 출력해야 함
# 원하는 숫자를 만드는 방법은?
'''
Input: nums = [3,2,4], target = 6
Input: nums = [3,3], target = 6
Input: nums = [2,7,11,15], target = 9

'''

class Solution(object):

    # 브루트 포스로 계산
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # in을 이용한 탐색
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):  # index, num
            complement = target - n
            if complement in nums[i + 1:]:  # 나머지 배열에 데이터가 들어 있는가??
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

    # 첫번째 수를 뺀 결과 키 조회
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타켓에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [nums.index(num), nums_map[target - num]]

    # 첫번째 수를 뺀 결과 키 조회
    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

    # 투 포인터 이용
    # 투 포인터란? 왼쪽 포인터와 오른쪽 포인터의 합이 타켓보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정하는 방식
    # 그러나 정렬된 상태여야 함을 명시해야 한다.
    def twoSum5(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타켓보다 크면 오른쪽 포인터를 왼쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타켓보다 작으면 왼쪽 포인터를 오른쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]


solution = Solution()

nums = [2, 7, 11, 15]
target = 9

# O(n^2)
two_sum = solution.twoSum(nums, target)
print(two_sum)

# O(n)
two_sum2 = solution.twoSum2(nums, target)
print(two_sum2)

# 조회는 거의 O(1)
two_sum3 = solution.twoSum3(nums, target)
print(two_sum3)

# 조회는 거의 O(1)
two_sum4 = solution.twoSum4(nums, target)
print(two_sum4)
