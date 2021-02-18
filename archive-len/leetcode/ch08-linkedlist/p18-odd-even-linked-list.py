# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n) 에 풀이하라.

# 예제
# 1 > 2 > 3 > 4 > 5 > Null

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수 헤드로 변경
        odd.next = even_head
        return head
