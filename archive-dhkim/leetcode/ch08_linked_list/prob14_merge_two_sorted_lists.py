
"""
https://leetcode.com/problems/merge-two-sorted-lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_01:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        node_list = []

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node_list.append(l1)
                l1 = l1.next
            else:
                node_list.append(l2)
                l2 = l2.next

        while l1 is not None:
            node_list.append(l1)
            l1 = l1.next

        while l2 is not None:
            node_list.append(l2)
            l2 = l2.next

        for idx, node in enumerate(node_list[:-1]):
            node.next = node_list[idx + 1]

        if len(node_list) > 0:
            node_list[-1].next = None
            return node_list[0]

        return None


class Solution_02:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 둘 중 하나가 null이면 null이 아닌 노드 리턴
        if l1 is None and l2 is not None:
            return l2
        elif l2 is None and l1 is not None:
            return l1

        # 둘 다 null이면 null 리턴
        elif l1 is None and l2 is None:
            return None

        # 둘 다 값이 있으면 작은 노드만 커서 이동하여 재귀수행.
        # 현재 작은 노드의 next를 재귀 반환값으로 연결하고 현재 노드를 리턴
        else:
            if l1.val > l2.val:
                bigger, smaller = l1, l2
            else:
                bigger, smaller = l2, l1

            smaller.next = self.mergeTwoLists(bigger, smaller.next)

            return smaller
