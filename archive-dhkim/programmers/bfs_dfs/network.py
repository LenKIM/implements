from collections import defaultdict

"""
https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
"""


def solution(n, computers):
    answer = 0

    # 노드를 입력하면 연결된 노드들의 리스트를 반환하는 딕셔너리 생성
    link_dict = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                link_dict[i].append(j)

    # 노드 방문 여부를 기록할 리스트
    check_ary = [0 for _ in range(n)]

    # dfs 재귀 탐색 함수
    def dfs(idx):
        if check_ary[idx] == 0:
            check_ary[idx] = 1
            for link_idx in link_dict[idx]:
                dfs(link_idx)

    # 각 노드에 대해 dfs 재귀탐색 수행
    for p in range(n):
        # dfs로 탐색했는데 현재 노드가 처음 방문한 노드라면 새로운 네트워크가 발견된 것
        if check_ary[p] == 0:
            answer += 1
            dfs(p)

    return answer
