
"""
https://leetcode.com/problems/palindrome-linked-list
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if head is None:
            return True

        values = [head.val]

        tmp = head.next

        while tmp is not None:
            values.append(tmp.val)
            tmp = tmp.next

        return values == values[::-1]

