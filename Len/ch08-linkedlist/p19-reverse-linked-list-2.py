# 인덱스 m까지 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.
# 예제
# 1 > 2 > 3 > 4 > 5 > Null
# m = 2, n = 4

# 1 > 4 > 3 > 2 > 5 > Null

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 예외 처리
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(m - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
