from typing import List

"""
https://leetcode.com/problems/most-common-word
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        lower_str = paragraph.lower()

        for c in "!?',;.":
            lower_str = lower_str.replace(c, ' ')

        max_w = ''
        max_cnt = 0

        word_counter = {}
        for w in lower_str.split(' '):
            if w in banned or w == ' ' or not w:
                continue
            word_counter[w] = word_counter[w] + 1 if w in word_counter else 1

            if word_counter[w] > max_cnt:
                max_cnt = word_counter[w]
                max_w = w

        return max_w




