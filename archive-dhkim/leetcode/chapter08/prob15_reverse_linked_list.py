
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        stack = []

        while head is not None:
            stack.append(head)
            head = head.next

        if not stack:
            return None

        stack = stack[::-1]

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None

        return stack[0]


