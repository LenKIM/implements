from typing import List

'''
https://leetcode.com/problems/sort-colors/

Follow up:
Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?

1. 분할 정렬 - in place order 가 아니다.
2. 쿽 정렬

3가지 색상으로 정렬해야 한다.
'''


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def sort(low, high):
            if high <= low:
                return
            mid = partition(low, high)
            sort(low, mid - 1)
            sort(mid, high)

        def partition(low, high):
            pivot = nums[(low + high) // 2]
            while low <= high:
                while nums[low] < pivot:
                    low += 1
                while nums[high] > pivot:
                    high -= 1

                if low <= high:
                    nums[low], nums[high] = nums[high], nums[low]
                    low, high = low + 1, high - 1
            return low

        sort(0, len(nums) - 1)


solution = Solution()
l = [2,0,1]
solution.sortColors(l)

print(l)


def quickSort2(input: List[int]) -> list:
    if len(input) <= 1:
        return input

    pivot = input[0]

    less = list()
    more = list()
    equal = list()

    for idx in range(1, len(input)):
        if input[idx] < pivot:
            less.append(input[idx])
        else:
            more.append(input[idx])

    return quickSort2(less) + [equal] + quickSort2(more)