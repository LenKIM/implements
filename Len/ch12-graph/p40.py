from typing import List
import collections, heapq


class Solution:
    # 모든 노드가 신호를 받는 데 걸리는 시간
    # 모든 노드에 도달할 수 있는지 여부
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u,v,w in times:
            graph[u].append((v,w))

        # 큐 변수: [(소요시간, 정점)]
        Q = [(0, K)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt,v))
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())

        return -1