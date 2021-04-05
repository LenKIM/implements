from typing import List

"""
https://leetcode.com/problems/merge-intervals
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 각 범위들의 시작, 끝 값들을 값과 플래그(시작/끝 여부)의 튜플들로 매핑
        map_values = []
        for s, e in intervals:
            map_values.append((s, 1))
            map_values.append((e, 2))

        # 매핑된 값들을 1)값 2)플래그(시작이 먼저오게) 순으로 정렬
        map_values.sort(key=lambda a: (a[0], a[1]))

        # 시작/끝 여부를 스택으로 처리하며 중첩 처리된 범위 추출
        stack, result = [], []
        for val, flag in map_values:
            if flag == 1:
                stack.append(val)
            else:
                tmp = stack.pop(-1)
                if len(stack) == 0:
                    result.append([tmp, val])

        return result
