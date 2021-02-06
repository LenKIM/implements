
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
