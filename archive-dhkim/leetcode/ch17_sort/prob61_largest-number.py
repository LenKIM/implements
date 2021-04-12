from typing import List

"""
https://leetcode.com/problems/largest-number
"""


class Solution:
    # 로직을 처음부터 잘 못 설계함
    # def largestNumber_failed(self, nums: List[int]) -> str:
    #
    #     def func(str_nums, idx):
    #         # 탈출조건: 길이가 1이하
    #         if len(str_nums) <= 1:
    #             return str_nums
    #
    #         # 각 값들을 idx번째 숫자값으로 그룹화하기
    #         map_list = [[] for _ in range(10)]
    #         for str_n in str_nums:
    #             map_idx = int(str_n[idx])
    #             map_list[map_idx].append(str_n)
    #
    #         res = []
    #         for n_list in map_list[::-1]:
    #
    #             # 각 그룹에 대해 idx 다음번째 숫자값이 idx번째보가 큰것/작은것/없는것 분류
    #             upper, middle, lower = [], [], []
    #             for n in n_list:
    #                 pivot = int(n[idx])
    #                 if len(n) == idx + 1:
    #                     middle.append(n)
    #                 elif int(n[idx + 1]) > pivot:
    #                     upper.append(n)
    #                 else:
    #                     lower.append(n)
    #
    #             # idx+1값 기준으로 분류된 각 그룹들에 대해 재귀수행 분할정복
    #             local_res = func(upper, idx + 1) + func(middle, idx + 1) + func(lower, idx + 1)
    #             res += local_res
    #
    #         return res
    #
    #     str_nums = [str(n) for n in nums]
    #     res_strs = func(str_nums, 0)
    #
    #     return "".join(res_strs)

    def largestNumber(self, nums: List[int]) -> str:

        # 일반적인 퀵정렬과 같음. 두 값을 비교할 때 a+b 와 b+a 에 대해 대소비교하는 점만 다름
        def quick_sort(str_nums):
            if len(str_nums) <= 1:
                return str_nums

            pivot_idx = len(str_nums) // 2
            pivot = str_nums[pivot_idx]

            upper, same, lower = [], [], []
            for n in str_nums:
                if n == pivot:
                    same.append(n)
                elif pivot + n > n + pivot:
                    lower.append(n)
                else:
                    upper.append(n)

            return quick_sort(upper) + same + quick_sort(lower)

        # 문자열 타입으로 캐스팀
        cast_nums = [str(n) for n in nums]

        # 정렬
        sorted_nums = quick_sort(cast_nums)

        # 결과 리턴 ([0, 0] -> "00" 인 케이스가 있어서 int변환 후 다시 str 변환... 번거롭...)
        return str(int("".join(sorted_nums)))
