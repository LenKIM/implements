from typing import List

"""
https://leetcode.com/problems/permutations
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(data, acc):
            if len(acc) == len(nums):
                res.append(acc)
                return

            # 순열은 현재 레벨에서 다음 레벨로 data 넘길 때, 현재 값만 뺀 data를 넘긴다
            # 조합은 현재 값 이후의 data만 넘긴다
            for idx, n in enumerate(data):
                tmp_data = [a for in_idx, a in enumerate(data) if in_idx != idx]
                dfs(tmp_data, acc + [n])

        dfs(nums, [])

        return res

#     def permute(self, nums: List[int]) -> List[List[int]]:

#         results = []

#         def DFS(stack):
#             for d in nums:
#                 if d not in stack:
#                     DFS(stack + [d])

#             if len(stack) == len(nums):
#                 results.append(stack)

#         DFS([])

#         return results