import re

"""
https://leetcode.com/problems/valid-palindrome
"""


class Solution:
    def isPalindrome_01(self, s: str) -> bool:

        filter_s = "".join(
            [a.lower() for a in s if ord(a) in range(65, 91) or ord(a) in range(97, 123) or ord(a) in range(48, 58)])

        for i in range(len(filter_s) // 2):
            if filter_s[i] != filter_s[-1 - i]:
                return False

        return True

    def isPalindrome_02(self, s: str) -> bool:
        ps = re.sub('[^a-zA-Z0-9]', '', s).lower()

        return ps == ps[::-1]