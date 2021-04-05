from typing import List

"""
https://leetcode.com/problems/reverse-string
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # s = s.reverse()

        pointer = 0

        while pointer < len(s) // 2:
            tmp = s[pointer]
            s[pointer] = s[len(s) - pointer - 1]
            s[len(s) - pointer - 1] = tmp
            pointer += 1
