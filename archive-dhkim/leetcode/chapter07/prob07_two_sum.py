from typing import List

"""
https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """
        O(n^2) 나이브한 해결
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                sum_value = nums[i] + nums[j]

                if sum_value == target:
                    return [i, j]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """
        O(n) 해결법. 숫자->인덱스 딕셔너리 이용
        :param nums:
        :param target:
        :return:
        """
        num2idx_dict = dict()

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in num2idx_dict.keys():
                return [num2idx_dict[diff], idx]

            num2idx_dict[num] = idx