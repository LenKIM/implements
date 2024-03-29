# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 1
    # def sortList(self, head: ListNode) -> ListNode:
    #     # Simple Answer
    #     if not head:
    #         return head
    #
    #     simple_list = []
    #     while head:
    #         simple_list.append(head.val)
    #         head = head.next
    #     simple_list.sort()
    #
    #     root = ListNode()
    #     temp = root
    #     for idx, val in enumerate(simple_list):
    #         root.val = val
    #         if idx != len(simple_list) - 1:
    #             root.next = ListNode()
    #             root = root.next
    #
    #     return temp

    # 2
    # def sortList(self, head: ListNode) -> ListNode:
    #     def heapSort(list: ListNode):
    #         root = list
    #         if not root:
    #             return root
    #
    #         simple_list = []
    #         while root:
    #             simple_list.append(root.val)
    #             root = root.next
    #
    #         heapq.heapify(simple_list)
    #
    #         root_for_return = ListNode()
    #         temp = root_for_return
    #         while simple_list:
    #             heappop = heapq.heappop(simple_list)
    #             root_for_return.val = heappop
    #             if simple_list:
    #                 root_for_return.next = ListNode()
    #                 # 아래 있고 없고가 temp 의 위치를 좌우한다? 왜?
    #                 root_for_return = root_for_return.next
    #         return temp
    #
    #     return heapSort(head)
    # 3 mergeSort
    # 머지 정렬(책 정답)
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # 런너 기법 활용
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2);

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next,l2)
        return l1 or l2
###########

solution = Solution()
node = ListNode(3, ListNode(1, ListNode(2, ListNode(4))))

sort_list = solution.sortList(node)
print(sort_list)

