"""
https://programmers.co.kr/learn/courses/30/lessons/43165
"""


def solution(numbers, target):
    answer = 0

    def dfs(idx, acc):
        if idx == len(numbers):
            if acc == target:
                return 1
            else:
                return 0

        neg_dfs = dfs(idx + 1, acc - numbers[idx])
        pos_dfs = dfs(idx + 1, acc + numbers[idx])

        return neg_dfs + pos_dfs

    answer = dfs(0, 0)

    return answer
