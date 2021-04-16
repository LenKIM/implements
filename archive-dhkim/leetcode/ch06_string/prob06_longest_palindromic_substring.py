
"""
https://leetcode.com/problems/longest-palindromic-substring
"""


class Solution01:
    """
    예전에 제출했던 답안.
    """
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


class Solution02:
    """
    약간의 성능 개선을 위해, 각 윈도우는 매번 최소 사이즈에서 확장하지 않고 앞선 최대 길이에서부터 확장한다
    """
    def longestPalindrome(self, s: str) -> str:

        # 예외처리
        if len(s) < 2 or s == s[::-1]:
            return s

        def is_palin(str_dat, s_idx, e_idx):
            if 0 <= s_idx and e_idx < len(str_dat):
                sub_str_dat = str_dat[s_idx: e_idx + 1]
                if sub_str_dat == sub_str_dat[::-1]:
                    return True

            return False

        w2_s, w2_e = 1, 0
        w3_s, w3_e = 1, 1

        res_panlin = ""

        for i in range(len(s)):

            while is_palin(s, i - w2_s, i + w2_e):
                res_panlin = max(res_panlin, s[i - w2_s: i + w2_e + 1], key=len)
                w2_s += 1
                w2_e += 1

            while is_palin(s, i - w3_s, i + w3_e):
                res_panlin = max(res_panlin, s[i - w3_s: i + w3_e + 1], key=len)
                w3_s += 1
                w3_e += 1

        return res_panlin


class Solution03:
    """
    답안에 가까운 풀이. 매 인덱스에서 최소 윈도우사이즈부터 확장해나가되, 각 윈도우에선 양 끝의 값끼리만 비교한다.
    """
    def longestPalindrome(self, s: str) -> str:

        # 예외처리
        if len(s) < 2 or s == s[::-1]:
            return s

        def expand(s, start, end):
            while 0 <= start and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1:end]

        max_panlin = ""

        for idx in range(len(s) - 1):
            max_panlin = max(max_panlin, expand(s, idx, idx + 1), expand(s, idx, idx + 2), key=len)

        return max_panlin


class LongestCommonSubstring:
    """
    최장 공통 부분 문자열(Longest Common Substring) 문제
    두 문자열에 공통으로 존재하는 부분문자열 중 가장 긴 부분문자열을 찾는 문제이다.
    가로가 s1, 세로가 s2인 이차원 매트릭스를 만들어 서로 같은 문자의 칸에 1을 표기한다. 대각선으로 연속되는 1의 길이가 가장 긴 것을 찾는다.
    """
    def largest_common_substring(self, s1: str, s2: str):
        matrix = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

        max_len_idx_tuple = (0, 0)  # len and s1-idx

        for s2_idx, s2_c in enumerate(s2):

            for s1_idx, s1_c in enumerate(s1):
                if s1_c == s2_c:
                    if 0 < s2_idx and 0 < s1_idx and matrix[s2_idx-1][s1_idx-1] > 0:
                        matrix[s2_idx][s1_idx] = matrix[s2_idx-1][s1_idx-1] + 1
                    else:
                        matrix[s2_idx][s1_idx] = 1

                    max_len_idx_tuple = max(max_len_idx_tuple, (matrix[s2_idx][s1_idx], s1_idx), key=lambda a: a[0])

        max_len, max_idx = max_len_idx_tuple

        return s1[max_idx - (max_len - 1):max_idx + 1]




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


