from typing import List

"""
https://leetcode.com/problems/k-closest-points-to-origin/submissions/
"""


class MinHeap:

    def __init__(self):
        self.heap = [(None, [0,0])]

    def insert(self, point):
        dist = point[0]**2 + point[1]**2
        self.heap.append((dist, point))

        idx = len(self.heap) - 1
        while idx >= 2 and self.heap[idx][0] < self.heap[idx // 2][0]:
            tmp_tup = self.heap[idx]
            self.heap[idx] = self.heap[idx // 2]
            self.heap[idx // 2] = tmp_tup

            idx = idx // 2

    def extract(self):
        if len(self.heap) <= 1:
            return None

        min_tup = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap = self.heap[:-1]

        idx = 1
        while idx < len(self.heap):
            parent = self.heap[idx][0]
            left = self.heap[idx*2][0] if idx*2 < len(self.heap) else None
            right = self.heap[idx*2+1][0] if idx*2+1 < len(self.heap) else None

            if (left and left < parent) or (right and right < parent):
                child_idx = idx*2 if (left and right and left < right) or not right else idx*2+1

                tmp_tup = self.heap[idx]
                self.heap[idx] = self.heap[child_idx]
                self.heap[child_idx] = tmp_tup

                idx = child_idx
            else:
                break

        return min_tup[1]


class Solution:
    # def kClosest_01(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     return sorted(points, key=lambda a: a[0]**2 + a[1]**2)[:k]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_tree = MinHeap()
        for point in points:
            heap_tree.insert(point)

        res = []
        for _ in range(k):
            res.append(heap_tree.extract())

        return res


if __name__ == "__main__":
    solution = Solution()
    res = solution.kClosest(
        points=[[0,1],[1,0]],
        k=2
    )

    print(f">> res:")
    print(res)
