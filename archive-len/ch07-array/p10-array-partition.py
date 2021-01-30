# 배열 파티션 1
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
from typing import List


class Solution(object):
    # 오름차순 풀이
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum

    # 짝수번째 값 계산
    def arrayPairSum2(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n
        return sum
    # 파이썬다운 방식
    def arrayPairSum3(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


solution = Solution()

input = [1, 4, 3, 2]

pair_sum = solution.arrayPairSum(input)
pair_sum2 = solution.arrayPairSum2(input)
print(pair_sum)
print(pair_sum2)
