#!/bin/python3
import collections
import os


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return self.prev + " | " + self.data + " | " + self.next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# def reverse(node: ListNode, prev: ListNode = None):
#     if not node:
#         return prev
#     next, node.next = node.next, prev
#     return reverse(next, node)
#
# return reverse(head)
def reverse(head: DoublyLinkedListNode):
    node, prev, temp_next = head, None, None

    while node:
        # temp_next, node.next = node.next, temp_prev
        # temp_prev, node = node, temp_next

        temp_next, node.next = node.next, prev
        prev, node = node, temp_next

    return prev


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)
        print(llist1)
        # print_doubly_linked_list(llist1, ' ', fptr)
        # fptr.write('\n')
    #
    # fptr.close()
