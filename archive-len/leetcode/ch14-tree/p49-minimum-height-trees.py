import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n <= 1:
            return [0]
        graph = collections.defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i) # 마지막 leaf가 한 개

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves


solution = Solution()
solution.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
