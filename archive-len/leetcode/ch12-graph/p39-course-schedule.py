# dfs로 사이클이 있는지 확인하는 코드
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # 순환 구조를 파악하기위해 이미 방문했던 노드는 traced 변수에 저장
        traced = set()

        def dfs(i):

            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):

            # 순환 구조
            if i in traced:
                return False

            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True




