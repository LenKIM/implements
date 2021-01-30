
"""
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:

        mapper = {')': '(', '}': '{', ']': '['}

        stack = []

        for c in s:
            if c in mapper.keys():
                if len(stack) == 0:
                    return False
                last_added = stack.pop()

                if mapper[c] != last_added:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        return False
