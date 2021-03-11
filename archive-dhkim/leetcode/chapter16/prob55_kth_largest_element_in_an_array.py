from typing import List

"""
https://leetcode.com/problems/kth-largest-element-in-an-array
"""


class MaxHeap:

    def __init__(self, nums=None):
        self.heap_ary = []

        if nums:
            for n in nums:
                self.insert(n)

    def swap(self, p_idx, c_idx):
        if self.heap_ary:
            tmp = self.heap_ary[p_idx]
            self.heap_ary[p_idx] = self.heap_ary[c_idx]
            self.heap_ary[c_idx] = tmp

    def insert(self, num):
        # 1. 힙배열의 맨 끝에 num 추가
        self.heap_ary.append(num)
        # print(self.heap_ary)

        # 2. (loop) 맨 끝에서부터 부모와 비교하여 heapify
        child_idx = len(self.heap_ary) - 1
        parent_idx = (child_idx + 1) // 2 - 1

        while parent_idx >= 0 and self.heap_ary[parent_idx] < self.heap_ary[child_idx]:
            # swap
            self.swap(parent_idx, child_idx)

            # 부모자식 인덱스 갱신
            child_idx = parent_idx
            parent_idx = (child_idx + 1) // 2 - 1
            # print(self.heap_ary)

    def get_updated_p_c_indexes(self, p_idx):
        left_idx = (p_idx + 1) * 2 - 1
        right_idx = (p_idx + 1) * 2

        return p_idx, left_idx, right_idx

    def extract(self):
        # 1. 힙 루트 추출 및 맨 마지막 값으로 대체
        heap_max = self.heap_ary[0]
        self.heap_ary[0] = self.heap_ary[-1]
        self.heap_ary = self.heap_ary[:-1]
        # print(self.heap_ary)

        # 2. (loop) 맨 앞에서부터 자식과 비교하여 heapify
        parent_idx, left_idx, right_idx = self.get_updated_p_c_indexes(0)

        while True:
            valid_children = [(i, self.heap_ary[i]) for i in [left_idx, right_idx] if i < len(self.heap_ary)]
            if not valid_children:
                break

            max_child_idx = max(valid_children, key=lambda a: a[1])[0]

            if self.heap_ary[parent_idx] < self.heap_ary[max_child_idx]:
                self.swap(parent_idx, max_child_idx)
                parent_idx, left_idx, right_idx = self.get_updated_p_c_indexes(max_child_idx)
                # print(self.heap_ary)
            else:
                break

        return heap_max


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MaxHeap(nums)

        max_val = None
        for _ in range(k):
            max_val = heap.extract()

        return max_val
