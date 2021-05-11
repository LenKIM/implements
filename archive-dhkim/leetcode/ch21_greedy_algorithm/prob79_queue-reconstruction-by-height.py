from typing import List

"""
https://leetcode.com/problems/queue-reconstruction-by-height
"""


class Solution:
    """
    우선 people 리스트의 원소들을 "(1) k값 기준 asc, (2) h값 기준 asc" 로 정렬한 뒤 차례대로 merge_list에 입력한다.
    입력할 때의 조건은
    (1) 기존 merge_list에서 입력할 값의 h 이상인 것들 중 k번째 인덱스를 파악
    (2) 찾은 인덱스 뒤에 입력하는데 뒤의 원소의 k가 현재 원소의 k와 같지 않을 때까지 뒤로 이동하여 입력한다. (앞서 입력한 원소의 k조건을 건드리지 않기 위해)


    O(n^2)의 greedy한 풀이 복잡도이나 accepted됨...(더 나은 시간복잡도는 불가능한듯?)
    runtime : 668 ms
    memory : 14.8 MB
    """
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        # 1. people의 원소들을 k기준 그룹화하고, 각 그룹은 h 기준 asc 정렬
        people.sort(key=lambda a: (a[1], a[0]))

        merge_list = []

        # 2. 원소들을 하나씩 입력
        for h, k in people:
            gte_idx_list = []

            # 2-1. merge_list에서 값이 현재 h 이상인 것들 파악하기
            for idx, (in_h, in_k) in enumerate(merge_list):
                if in_h >= h:
                    gte_idx_list.append(idx)

                if len(gte_idx_list) == k:
                    break

            # 2-2. 이상인 것들 중 앞의 k번째 뒤면서, k 값이 같지 않은 것 뒤에 입력
            target_idx = gte_idx_list[-1] + 1 if gte_idx_list else 0

            while target_idx < len(merge_list) and merge_list[target_idx][1] == k:
                target_idx += 1

            merge_list.insert(target_idx, [h, k])

        return merge_list
