
"""
https://leetcode.com/problems/add-two-numbers
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        tmp = ListNode()
        root = tmp
        decimal_upper = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_val = l1_val + l2_val + decimal_upper
            decimal_upper = sum_val // 10
            decimal_least = sum_val % 10

            tmp.next = ListNode(decimal_least)
            tmp = tmp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if decimal_upper != 0:
            tmp.next = ListNode(decimal_upper)

        return root.next