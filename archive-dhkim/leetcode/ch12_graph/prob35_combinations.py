from typing import List

"""
https://leetcode.com/problems/combinations
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = [i + 1 for i in range(n)]
        res = []

        def dfs(data, acc):

            if len(acc) == k:
                res.append(acc)
                return

            # 순열은 현재 레벨에서 다음 레벨로 data 넘길 때, 현재 값만 뺀 data를 넘긴다
            # 조합은 현재 값 이후의 data만 넘긴다
            for idx, n in enumerate(data):
                tmp_data = [a for in_idx, a in enumerate(data) if in_idx > idx]
                dfs(tmp_data, acc + [n])

        dfs(nums, [])

        return res

#     def combine(self, n: int, k: int) -> List[List[int]]:
#         results = []
#         data = [i+1 for i in range(n)]

#         def DFS(stack, data, k):
#             for i, d in enumerate(data):
#                 if d not in stack and len(stack) < k:
#                     DFS(stack + [d], data[i+1:], k)

#             if len(stack) == k:
#                 results.append(stack)

#         DFS([], data, k)

#         return results
