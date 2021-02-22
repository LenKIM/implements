from typing import List
from collections import defaultdict

"""
https://leetcode.com/problems/minimum-height-trees

Linked List 없이 DFS 재귀 탐색 및 메모이제이션으로 노드별 최대 깊이 구하기
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if not edges:
            return [0]

        vertex2neighbors = defaultdict(list)
        for vertexes in edges:
            vertex2neighbors[vertexes[0]].append(vertexes[1])
            vertex2neighbors[vertexes[1]].append(vertexes[0])

        memoization = defaultdict(dict)

        def get_max_depth(now_v, pre_v):
            neighbors = [v for v in vertex2neighbors[now_v] if v != pre_v]
            if not neighbors:
                return 0

            depth_list = []
            for nb in neighbors:
                if nb in memoization[now_v]:
                    depth = memoization[now_v][nb]
                else:
                    depth = get_max_depth(nb, now_v) + 1
                    memoization[now_v][nb] = depth

                depth_list.append(depth)

            return max(depth_list)

        vertex2depths = defaultdict(list)
        for v in vertex2neighbors.keys():
            d = get_max_depth(v, -1)
            vertex2depths[d].append(v)

        # print(vertex2depths)

        return sorted(vertex2depths.items(), key=lambda t: t[0])[0][1]


if __name__ == "__main__":
    solution = Solution()
    res = solution.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
    print(f">> res : {res}")
