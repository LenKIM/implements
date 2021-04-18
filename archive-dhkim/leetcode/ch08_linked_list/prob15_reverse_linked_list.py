"""
https://leetcode.com/problems/reverse-linked-list/submissions/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution01:
    """
    연결리스트를 순회하면서 각 ListNode 객체를 list에 저장하고 연결을 뒤집는 방식
    단순무식한 방식인데 오히려 아래 재귀방식이나 반복문 방식보다 더 빠르고 메모리도 적게 사용한다... 왜?
    > 소요시간: 24 ms
    > 메모리: 15.6 MB
    """
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


class Solution02:
    """
    재귀를 이용하여 현재노드, 이전노드를 전달하며 매 재귀에서 연결을 뒤집고, 마지막 노드에 도달하면 해당 노드를 반환하는 방식
    > 소요시간: 32 ms
    > 메모리: 20.4 MB
    """
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        def recur(node: ListNode, prev: ListNode) -> ListNode:
            next_node = node.next
            node.next = prev

            if next_node is not None:
                return recur(next_node, node)
            else:
                return node

        return recur(head, None)


class Solution03:
    """
    반복문으로 연결 뒤집기
    > 소요시간: 36 ms
    > 메모리: 15.5 MB
    """
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        node = head

        while node:
            tmp = node.next
            node.next = prev

            prev = node
            node = tmp

        return prev





