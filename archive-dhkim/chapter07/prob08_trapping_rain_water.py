from typing import List

"""
https://leetcode.com/problems/trapping-rain-water
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        # height의 첫 번째 원소로 미리 초기화
        stack = [0]  # 솟은 기둥들의 인덱스를 저장할 스택
        max_idx = 0  # 스택 중에서 가장 높은 기둥의 인덱스

        for idx, num in enumerate(height):
            # 첫 원소는 패스
            if idx == 0:
                continue

            # num이 높은 기둥일 경우: (앞의 값보다 크면)
            if height[idx - 1] < num:

                # stack에서 가장 높은 기둥이 num 이하일 경우 -> 스택 비우고 빗물 계산
                if height[max_idx] <= num:
                    for tmp_idx in range(max_idx + 1, idx):
                        rain = height[max_idx] - height[tmp_idx]
                        result += max(rain, 0)
                    max_idx = idx  # 현재 기둥을 제일 높은 기둥으로 갱신
                    stack = [idx]  # 스택 비움

                # 그 외에는 스택에서 현재 기둥보다 낮은 것들 빼내고 현재 기둥 추가
                else:
                    while len(stack) > 0 and height[stack[-1]] < num:
                        stack.pop()
                    stack.append(idx)

                    # 기둥이 하나 뿐이면 빗물이 안 모임. 앞서 계산한 빗물량 반환
        if len(stack) <= 1:
            return result

        # 스택에 남은 것들에 대해 빗물 계산
        tmp = stack.pop()
        while len(stack) > 0:
            for cursor in range(stack[-1] + 1, tmp):
                rain = height[tmp] - height[cursor]
                result += max(rain, 0)
            tmp = stack.pop()

        return result

        # for num in height:
        #     if num이 높은 기둥일 경우: (앞의 값보다 크면)

        #         if stack에서 가장 높은 기둥이 num 이하일 경우:
        #             num부터 stack의 가장 높은기둥까지 빗물 계산하고 stack 비우기
        #             stack.push(num)
        #             max_height = num
        #         while 기존 stack에서 num보다 더 높은 기둥이 나올때까지
        #             stack.pop()
        #         stack.push()
        #
        # if stack 크기가 1 이하면 그대로 계산한 값 반환
        #
        # tmp = stack.pop()
        # while stack이 빌 때까지:
        #     stack의 마지막 기둥~tmp 기둥 사이의 빗물 계산
        #
        #
        # 계산값 반환








