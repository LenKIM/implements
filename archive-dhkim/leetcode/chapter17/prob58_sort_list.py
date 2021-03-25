"""
https://leetcode.com/problems/sort-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        values.sort()

        root = ListNode()
        tmp = root

        for v in values:
            tmp.next = ListNode(v)
            tmp = tmp.next

        return root.next
