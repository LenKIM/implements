import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, kk: int):
            if kk == 0:
                results.append(elements[:])

            # 자신 이전의 모든 값을 고정해서 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, kk - 1)
                elements.pop()

        dfs([], 1, k)
        return results

    def combine2(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))

