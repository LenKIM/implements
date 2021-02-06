
"""
https://leetcode.com/problems/longest-palindromic-substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 3 and s == s[::-1]:
            return s

        def expand(i, j):
            panlindrome = ""
            while 0 <= i and j < len(s):
                tmp = s[i: j + 1]
                if tmp == tmp[::-1]:
                    panlindrome = tmp
                    i -= 1
                    j += 1
                else:
                    break

            return panlindrome

        longest = ""
        for i, c in enumerate(s):
            longest = max(longest, expand(i, i + 1), expand(i, i + 2), key=len)

        if longest == "" and len(s) > 0:
            return s[-1]

        return longest

#     def longestPalindrome(self, s: str) -> str:
#         stack = []
#         palindrome = ""
#         longest = ""

#         if len(s) <= 1:
#             return s

#         for c in s:
#             if len(stack) >= 1 and stack[-1] == c:
#                 stack.pop()
#                 palindrome = c + palindrome + c
#             elif len(stack) >= 2 and palindrome == "" and stack[-1] != c and stack[-2] == c:
#                 a = stack.pop()
#                 b = stack.pop()
#                 palindrome = b + a + b
#             else:
#                 stack.append(c)                
#                 longest = longest if len(longest) > len(palindrome) else palindrome
#                 palindrome = ""

#         longest = longest if len(longest) > len(palindrome) else palindrome

#         if longest == "" and len(stack) > 0:
#             longest = stack[-1]

#         return longest


