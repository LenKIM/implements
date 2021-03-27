'''
 https://programmers.co.kr/learn/courses/30/lessons/43162
'''
from typing import List


def dfs(i, computers, visited):

    if visited[i]:
        return 0

    visited[i] = True
    for idx, value in enumerate(computers[i]):
        if computers[i][idx] == 1:
            dfs(idx, computers, visited)

    return 1

def solution(n, computers: List):
    answer = 0

    visited = [False] * n
    for idx, val in enumerate(computers):
        if not visited[idx]:
            answer += dfs(idx, computers, visited)

    return answer


i = solution(3, [[1, 1, 0],
                 [1, 1, 1],
                 [0, 1, 1]])
print(i)
