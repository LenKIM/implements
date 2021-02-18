# 연결 리스트를 입력받아 페어 단위로 스왑하라

# 입력 > 1,2,3,4
# 출력 > 2,1,4,3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # 연결리스트를 활용한 풀이
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head

    def swapPairs2(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next

    def swapPair3(self, head:ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받기
            head.next = self.swapPair3(p.next)
            p.next = head
            return p
        return head