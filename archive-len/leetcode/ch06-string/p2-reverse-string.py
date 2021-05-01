from typing import List
"""
https://leetcode.com/problems/reverse-string/
"""

class Solution:
    def reverse_string(self, s: List[str]) -> None:
        # 투 포인터를 이용한 스왑
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # 파이썬다운 방식
        s.reverse()
