import collections
import heapq
from typing import List


class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dest: int, K: int):
        graph = collections.defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v,w))

        Q = [(0, src,K)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dest:
                return price

            if k >= 0:
                for v,w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt,v,k-1))
        return -1
