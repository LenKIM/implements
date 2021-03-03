#!/bin/python3

"""
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
"""

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


# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    node_set1 = set()
    while head1:
        node_set1.add(str(head1))
        head1 = head1.next

    while head2:
        if str(head2) in node_set1:
            return head2.data
        head2 = head2.next

    return None


if __name__ == '__main__':
    fp = open("input01.txt", "r")

    tests = int(fp.readline())

    for tests_itr in range(tests):
        index = int(fp.readline())

        llist1_count = int(fp.readline())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(fp.readline())
            llist1.insert_node(llist1_item)

        llist2_count = int(fp.readline())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(fp.readline())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next

        for i in range(llist2_count):
            if i != llist2_count - 1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        print(str(result))
