from typing import List

"""
https://leetcode.com/problems/daily-temperatures
"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        pocket = [0]

        result = [0 for _ in range(len(T))]

        # 순서대로 숫자들을 보따리에 쌓아가면서 현재값과 비교
        # 보따리의 가장 최근값보다 현재값이 높을 경우, 보따리를 뒤로 타고가면서 비우기
        for idx, num in enumerate(T[1:]):
            idx = idx + 1

            # 내 보따리의 마지막 값과 현재 num의 값 비교
            # 현재값이 더 크면 보따리에서 더 큰값이 나올때까지 역순으로 비워야 한다.
            while pocket and T[pocket[-1]] < num:
                pop_idx = pocket.pop()
                result[pop_idx] = idx - pop_idx

            # 현재값을 보따리에 추가
            pocket.append(idx)

        return result
