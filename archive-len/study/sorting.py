
from typing import List
'''
https://hsp1116.tistory.com/33
'''
# 선택정렬
def selectionSort(input: List):
    for i_idx in range(0, len(input) - 1):
        temp = i_idx
        for j_idx in range(i_idx + 1, len(input)):
            if input[temp] >= input[j_idx]:
                temp = j_idx

        input[temp], input[i_idx] = input[i_idx], input[temp]
    return input

# 삽입정렬

def insertionSort(input: List):
    for i in range(1, len(input)):
        key = input[i]
        j = i - 1
        while j >= 0 and key < input[j]:
            input[j], input[j+1] = input[j+1], input[j]
            j = j - 1

        input[j+1] = key

    return input

# 버블정렬

def bubbleSort(input: List):
    for i in range(0, len(input)-1):
        for j in range(1, len(input)-i):
            if input[j-1] > input[j]:
                input[j-1], input[j] = input[j], input[j-1]

    return input

# 합병정렬

def merge(inut, s, e, m):

    temp_list = list()
    i = s
    j = m+1
    copy = 0

    while i <= m and j <=e:
        pass


def mergeSort(inut: List, s, e):
    if s<e:
        m = (s+e) / 2

        mergeSort(inut, m, s)
        mergeSort(inut, m + 1, s)
        merge(inut, s, e, m)

# 쿽정렬


if __name__ == '__main__':
    # sort = selectionSort([3, 2, 1])
    # sort = insertionSort([3, 2, 1])
    sort = bubbleSort([3, 2, 1])
    print(sort)