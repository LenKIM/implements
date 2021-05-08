"""

https://leetcode.com/problems/longest-repeating-character-replacement/
대문자로 구성된 문자열 s가 주어졌을 때 k번 만큼의 변경으로 만들 수 있는,
연속으로 반복된 문자열의 가장 긴 길이를 출력하라

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

"""


# AABABBA
#
from collections import Counter


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        # 가장 많이 사용된 값이 유리?
        right = left = 0

        counter = Counter()
        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counter.most_common(1)[0][1]

            # 가장 흔하게 등장하는 문자를 카운트하는데, 오른쪽 - 왼쪽 - 흔문자 가 k보다 크다는건,
            # 교체할 수 있는 조건이 더이상 성립되지 않는다.
            # 그러므로, 가장 왼쪽의 값을 뺀다.
            if right - left - max_char_n > k:
                counter[s[left]] -= 1
                left += 1
        return right - left


# def characterReplacement(self, s, k):
#     result, max_count = 0, 0
#     count = collections.Counter()
#     for i in xrange(len(s)):
#         count[s[i]] += 1
#         max_count = max(max_count, count[s[i]])
#         if result - max_count >= k:
#             count[s[i-result]] -= 1
#         else:
#             result += 1
#     return result


Solution().characterReplacement("AABABBA", 1)
