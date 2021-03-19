import collections
import heapq
from typing import List


class BinaryHeap(object):

    def __init__(self):
        self.items = [None]

    # 0을 사용하지 않기 때문에.
    def __len__(self):
        return len(self.items) - 1

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def percolate_up(self):
        l = len(self)
        p = l // 2

        while p > 0:
            if self.items[l] < self.items[p]:
                self.items[p], self.items[l] = self.items[l], self.items[p]

            l = p
            p = l // 2

    def extracted(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.percolate_down(1)
        return extracted

    def percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self.percolate_down(smallest)

import heapq

# def solution(scoville: List, K):
#
#     # heap = BinaryHeap()
#     sorted_list = list()
#     for v in scoville:
#         heapq.heappush(sorted_list, v)
#
#     answer = 0
#
#     while sorted_list[0] < K:
#         extracted = heapq.heappop(sorted_list)
#         heap_extracted = heapq.heappop(sorted_list)
#         smallest_ = extracted + (heap_extracted * 2)
#         heapq.heappush(sorted_list, smallest_)
#         answer = answer + 1
#
#     if answer == 0:
#         return -1
#     return answer


def checkIfValidScoville(sco: List, k):
    for s in sco:
        if s < k:
            return True
    return False

# i = solution([1, 2, 3, 9, 10, 12], 7)
# print(i)


def solution(scoville: List, K):
    heapq.heapify(scoville)
    answer = 0

    # heap = BinaryHeap()

    while scoville[0] < K:
        if len(scoville) > 1:
            extracted = heapq.heappop(scoville)
            heap_extracted = heapq.heappop(scoville)
            smallest_ = extracted + (heap_extracted * 2)
            heapq.heappush(scoville, smallest_)
            answer = answer + 1
        else:
            return -1

    return answer

