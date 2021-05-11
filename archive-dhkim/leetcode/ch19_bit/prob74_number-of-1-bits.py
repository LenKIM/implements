"""
https://leetcode.com/problems/number-of-1-bits/submissions/
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            cnt = cnt + (n % 2)
            n = n // 2

        return cnt
