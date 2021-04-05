"""
https://leetcode.com/problems/odd-even-linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_root = head.next

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = even_root

        return head
