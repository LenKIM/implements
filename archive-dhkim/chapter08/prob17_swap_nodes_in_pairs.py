

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = ListNode()
        root = prev
        prev.next = head

        while head and head.next:
            # 현재 두 페어 시프트
            tmp = head.next
            head.next = tmp.next
            tmp.next = head

            # 이전 페어의 노드가 현재의 tmp 노드를 가리키도록
            prev.next = tmp

            # 다음 페어로 이동
            head = head.next
            prev = tmp.next

        return root.next
