import collections
import sys

'''
https://leetcode.com/problems/minimum-window-substring/

문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 원도우를 찾아라.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

O(n) 으로 찾아라.
q 에다가 idx 넣고,
1. 3개의 값이 일치 할때
    = 길이 계산
2. 다음 "ABC"중 하나가 포함된 값이 나올 경우, 앞에서 포함된 값을 빼고, 크기 비교.

3. 반복 하면서 가장 작은 값을 찾으면 되지 않을까?  

## 못풀었음. 답안 참조
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end-start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1

        return s[start:end]


Solution().minWindow("ADOBECODEBANC", "ABC")

# import collections
# import sys
#
# '''
# 문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 원도우를 찾아라.
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
#
# O(n) 으로 찾아라.
# q 에다가 idx 넣고,
# 1. 3개의 값이 일치 할때
#     = 길이 계산
# 2. 다음 "ABC"중 하나가 포함된 값이 나올 경우, 앞에서 포함된 값을 빼고, 크기 비교.
#
# 3. 반복 하면서 가장 작은 값을 찾으면 되지 않을까?
#
# '''
#
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dict = collections.defaultdict(int)
        target = sorted(t)

        min_value = sys.maxsize
        result = ""
        for idx, val in enumerate(s):

            if val in t:

                if val in dict:
                    dict[val] = idx
                else:
                    dict[val] = idx

                # S = 'aa' T = 'aa'
                if sorted(str.join("", dict.keys())) == target:
                    dict_values_ = s[min(dict.values()): max(dict.values())+1]
                    if min_value > len(dict_values_):
                        min_value = len(dict_values_)
                        result = dict_values_

        return result
#
#
# # Solution().minWindow("ADOBECODEBANC", "ABC")
