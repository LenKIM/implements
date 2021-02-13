#!/bin/python3

import os


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

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

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head: DoublyLinkedListNode, data):

    target_node = DoublyLinkedListNode(data)
    if head is None:
        head = target_node

    elif data < head.data:
        target_node.next = head
        head.prev = target_node
        head = target_node

    else:
        answer = head

        while answer.next is not None and answer.data < data:
            answer = answer.next

        if answer.next is None and answer.data < data:
            answer.next = target_node
            target_node.prev = answer

        else:
            previous = answer.prev

            previous.next = target_node
            target_node.prev = previous

            target_node.next = answer
            answer.prev = target_node
    return head



    # temp = DoublyLinkedListNode(0)
    # answer = temp
    #
    # if head is None:
    #     return DoublyLinkedListNode(data)
    #
    # while True:
    #
    #     if head is None:
    #         break
    #
    #     target_node = DoublyLinkedListNode(data)
    #
    #     if head.data <= data and head.next is None:
    #         target_node.prev = temp.next
    #         temp = temp.next
    #         temp.prev = temp.prev.next
    #
    #     if head.data <= data and head.next.data > data:
    #         next_node = DoublyLinkedListNode(head.next.val)
    #
    #         target_node.prev = temp.next
    #         temp = temp.next
    #         temp.prev = temp.prev.next
    #
    #         temp.next = next_node.prev
    #         temp = temp.next
    #         temp.prev = temp.prev.next
    #
    #         head = head.next
    #
    #     else:
    #         node = DoublyLinkedListNode(head.data)
    #         node.prev = temp.next
    #         temp = temp.next
    #         temp.prev = temp.prev.next
    #
    #         head = head.next
    #
    # return answer.next

if __name__ == '__main__':

    t = 1

    for t_itr in range(t):
        llist_count = [1, 3, 4, 10]

        llist = DoublyLinkedList()

        for _ in llist_count:
            llist_item = int(_)
            llist.insert_node(llist_item)

        data = 5

        llist1 = sortedInsert(llist.head, data)
        print(llist1)
        # print_doubly_linked_list(llist1, ' ')