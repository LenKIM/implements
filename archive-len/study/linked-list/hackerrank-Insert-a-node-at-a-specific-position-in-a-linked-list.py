#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head: SinglyLinkedListNode, data, position):

    result = SinglyLinkedListNode(0)
    answer = result
    node = SinglyLinkedListNode(data)

    for idx in range(position):
        head_data = head.data
        head = head.next

        result.next = SinglyLinkedListNode(head_data)
        result = result.next

    if result is not None and result.next is not None:
        result_next = result.next
        result.next = node
        node.next = result_next

    if result is not None and result.next is None:
        result.next = node


    # node.next = head.next

    while True:
        if head is None:
            break

        temp_node = SinglyLinkedListNode(head.data)
        node.next = temp_node
        node = node.next
        head = head.next

    return answer.next

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
