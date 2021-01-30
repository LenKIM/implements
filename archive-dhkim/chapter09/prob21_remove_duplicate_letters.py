
"""
https://leetcode.com/problems/remove-duplicate-letters
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""

        charset = set(s)
        ordering = sorted(list(charset))

        for c in ordering:
            sub_str = s[s.index(c):]

            if charset == set(sub_str):
                next_str = sub_str.replace(c, '')
                return c + self.removeDuplicateLetters(next_str)

