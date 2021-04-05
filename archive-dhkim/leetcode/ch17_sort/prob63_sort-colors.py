from typing import List

"""
https://leetcode.com/problems/sort-colors
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quick_sort(ary, gte_idx, lte_idx) -> None:

            # 재귀 탈출조건
            if lte_idx - gte_idx < 1:
                return

            # 임의의 위치를 pivot으로 지정 (여기선 가운데 값)
            init_pivot_idx = (gte_idx + lte_idx) // 2

            #     print("test:", [str(p) if gte_idx <= p_idx <= lte_idx else "_" for p_idx, p in enumerate(ary)])
            # pivot 값을 맨 앞의 값과 swap한다 (순차적으로 읽으면서 pivot과 비교할거니까)
            ary[gte_idx], ary[init_pivot_idx] = ary[init_pivot_idx], ary[gte_idx]

            # gte_idx+1부터 차례로 읽으면서 pivot보다 작은 값이 있으면
            # 읽은 범위 내의 pivot보다 큰 값 중 맨 앞의 것과 swap해준다
            bigger_idx = gte_idx + 1
            for i in range(gte_idx + 1, lte_idx + 1):
                # 맨 앞의 pivot과 비교
                if ary[i] < ary[gte_idx]:
                    ary[i], ary[bigger_idx] = ary[bigger_idx], ary[i]
                    bigger_idx += 1
            #         print("test:", [str(p) if gte_idx <= p_idx <= lte_idx else "_" for p_idx, p in enumerate(ary)])

            # 맨 앞에 있던 pivot을 pivot보다 큰 범위의 바로 앞의 값과 swap
            ary[gte_idx], ary[bigger_idx - 1] = ary[bigger_idx - 1], ary[gte_idx]
            #     print("test:", [str(p) if gte_idx <= p_idx <= lte_idx else "_" for p_idx, p in enumerate(ary)])

            # recursion으로 좌우 분할정복
            pivot_idx = bigger_idx - 1
            quick_sort(ary, gte_idx, pivot_idx - 1)
            quick_sort(ary, pivot_idx + 1, lte_idx)

        quick_sort(nums, 0, len(nums) - 1)
