from collections import Counter

"""
https://leetcode.com/problems/longest-repeating-character-replacement/submissions/
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counter = Counter()
        left_idx = right_idx = 0
        res = 0

        for right_idx in range(1, len(s) + 1):
            c = s[right_idx - 1]

            counter[c] += 1

            # 현재 카운터 내애 가장 고빈도값
            most_freq_cnt = counter.most_common(1)[0][1]

            if right_idx - left_idx - most_freq_cnt > k:
                counter[s[left_idx]] -= 1
                left_idx += 1
            elif right_idx - left_idx - most_freq_cnt == k:
                res = max(res, right_idx - left_idx)

        res = max(res, right_idx - left_idx)

        return res
