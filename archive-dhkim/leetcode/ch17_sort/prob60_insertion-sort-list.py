"""
https://leetcode.com/problems/insertion-sort-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        root = ListNode(-5001)

        while head:
            prior = tmp = root
            while tmp and tmp.val < head.val:
                prior = tmp
                tmp = tmp.next

            new_node = ListNode(head.val)
            new_node.next = tmp
            prior.next = new_node

            head = head.next

        return root.next
