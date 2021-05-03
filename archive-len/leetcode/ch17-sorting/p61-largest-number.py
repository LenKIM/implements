from typing import List

# https://corikachu.github.io/articles/python/python-magic-method
# class aa(str):
#     def __lt__(self, other):
#         return self + other > other + self
#
#
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         l = list(map(str, nums))
#
#         l.sort(key=aa)
#         # print(l)
#
#         # 자리의 숫자가 작은게 앞으로 온다.
#
#         # 1. 글자별로 숫자가 가장 큰 부분이 앞으로
#         # 2. 그 다음부터는 숫자가 큰것대로
#         join = "".join(l)
#         return '0' if join[0] == '0' else join


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            # 숫자가 크다 가 아니라, 문자열 순서에 따라 비교되어야 한다.
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j = j - 1
            i += 1

        return str(int(''.join(map(str, nums))))

    @staticmethod
    def to_swap(param, param1):
        return str(param) + str(param1) < str(param1) + str(param)


solution = Solution()
# print(solution.largestNumber([10, 2]))
print(solution.largestNumber([3, 30, 34, 5, 53, 9]))
