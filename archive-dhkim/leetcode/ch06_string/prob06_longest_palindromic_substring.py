
"""
https://leetcode.com/problems/longest-palindromic-substring
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:

        def palindrome(full_str, start_idx, end_idx) -> str:
            if 0 <= start_idx and end_idx < len(full_str):
                sub_str = full_str[start_idx: end_idx + 1]
                if sub_str == sub_str[::-1]:
                    # 현재 부분문자열이 palindrome이면 좌우로 한 칸씩 확장하며 계속 검사
                    return max(sub_str, palindrome(full_str, start_idx - 1, end_idx + 1), key=len)

            return ""

        longest_palindrome = s[:1]  # 초기화: 한글자 짜리 회문
        for i in range(len(s)):
            palin_even = palindrome(s, i, i + 1)  # "aa"처럼 짝수 회문
            palin_odd = palindrome(s, i, i + 2)  # "aba"처럼 홀수 회문
            longest_palindrome = max(palin_even, palin_odd, longest_palindrome, key=len)

        return longest_palindrome

    # def longestPalindrome(self, s: str) -> str:
    #
    #     if len(s) <= 3 and s == s[::-1]:
    #         return s
    #
    #     def expand(i, j):
    #         panlindrome = ""
    #         while 0 <= i and j < len(s):
    #             tmp = s[i: j + 1]
    #             if tmp == tmp[::-1]:
    #                 panlindrome = tmp
    #                 i -= 1
    #                 j += 1
    #             else:
    #                 break
    #
    #         return panlindrome
    #
    #     longest = ""
    #     for i, c in enumerate(s):
    #         longest = max(longest, expand(i, i + 1), expand(i, i + 2), key=len)
    #
    #     if longest == "" and len(s) > 0:
    #         return s[-1]
    #
    #     return longest

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


