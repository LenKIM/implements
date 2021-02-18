# 자신을 제외한 배열의 곱
# 나누셈을 하지 않고 O(n)에 풀이하라
from typing import List


class Solution(object):
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셉
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out


solution = Solution()
input = [1,2,3,4]
solution.productExceptSelf(input)
