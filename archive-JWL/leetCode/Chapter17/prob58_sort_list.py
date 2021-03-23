# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def printList(self, head:ListNode):
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        print(list1)

    def merge1(self,node1:ListNode, node2:ListNode) ->ListNode:
        res = ListNode()
        head = res
        while node1 and node2:
            if node1.val < node2.val:
                res.next = node1
                node1 = node1.next
                res = res.next
            else:
                res.next = node2
                node2 = node2.next
                res = res.next
        if node1:
            res.next = node1
        else:
            res.next = node2
        self.printList(head)
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        runner1 = head
        runner2 = head

        if not (head and head.next):
            return head

        while runner2 and runner2.next:
            half, runner1, runner2 = runner1, runner1.next, runner2.next.next

        half.next = None

        self.printList(head)
        self.printList(runner1)
        print("----")
        result = self.merge1(self.sortList(head), self.sortList(runner1))

        return result



    def sortList(self, head: ListNode) -> ListNode:
        runner1 = head
        runner2 = head

        if not (head and head.next):
            return head

        while runner2 and runner2.next:
            half, runner1, runner2 = runner1, runner1.next, runner2.next.next

        half.next = None

        self.printList(head)
        self.printList(runner1)
        print("----")
        result = self.merge1(self.sortList(head), self.sortList(runner1))

        return result
