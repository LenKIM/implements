import heapq
from typing import List

"""
https://leetcode.com/problems/network-delay-time
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # a->b 가중치 딕셔너리로 변환
        weights = dict()
        for s, d, w in times:
            if s not in weights:
                weights[s] = [(d, w)]
            else:
                weights[s].append((d, w))

        distances = dict()                          # k에서 각 노드까지의 최단경로 딕셔너리
        queue = []                                  # bfs 탐색용 큐
        distances[k] = 0
        heapq.heappush(queue, (distances[k], k))

        while queue:
            cur_dist, cur_node = heapq.heappop(queue)
            # print(f"now cur_node:{cur_node}")

            if cur_node not in weights.keys():
                continue

            for tmp_node, tmp_weight in weights[cur_node]:
                new_dist = cur_dist + tmp_weight

                if tmp_node in distances and distances[tmp_node] <= new_dist:
                    continue

                distances[tmp_node] = new_dist
                if tmp_node in weights.keys():
                    heapq.heappush(queue, (new_dist, tmp_node))

        if len(distances) != n:
            return -1

        return max(distances.values())
