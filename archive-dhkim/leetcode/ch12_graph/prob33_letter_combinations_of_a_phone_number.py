from typing import List

"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        results = set()

        num2ary = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']        
        }

        print(num2ary[digits[0]])

        def dfs(i, con):

            if i == len(digits):
                results.add(con)
                return

            ary = num2ary[digits[i]]
            for c in ary:
                dfs(i+1, con+c)

        dfs(0, '')

        return list(results)