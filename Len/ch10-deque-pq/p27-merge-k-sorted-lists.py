# k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.
# [ 1->4->5, 1->3->4, 2->6 ]
# > 1->1->2->3->4->4->5->6
import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val
                                      , idx, result.next))

        return root.next


solution = Solution()

node, node.next, node.next.next = ListNode(1), ListNode(4), ListNode(5)
node1, node1.next, node1.next.next = ListNode(1), ListNode(3), ListNode(4)
node2, node2.next = ListNode(2), ListNode(6)

k_lists = solution.mergeKLists([node, node1, node2])
print(k_lists)
