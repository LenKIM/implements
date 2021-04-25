import collections
import sys

'''
문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 원도우를 찾아라.
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

O(n) 으로 찾아라.
q 에다가 idx 넣고,
1. 3개의 값이 일치 할때
    = 길이 계산
2. 다음 "ABC"중 하나가 포함된 값이 나올 경우, 앞에서 포함된 값을 빼고, 크기 비교.

3. 반복 하면서 가장 작은 값을 찾으면 되지 않을까?  

'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        target = sorted(t)
        counter = collections.Counter(t)
        result = ""
        dict = collections.defaultdict(list) # index 를 넣어준다.
        for idx, val in enumerate(s):

            if val in counter.keys():

                if counter[val] == 0:
                    dict[val].insert(0, idx)
                else:
                    counter[val] = counter[val] - 1
                    dict[val] = dict[val] + [idx]
                    dict[val] = sorted(dict[val])


                    ...
                    # dict_values_ = s[min(dict.values()): max(dict.values())+1]
                    # if min_value > len(dict_values_):
                    #     min_value = len(dict_values_)
                    #     result = dict_values_

        return result


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
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#
#         dict = collections.defaultdict(int)
#         target = sorted(t)
#
#         min_value = sys.maxsize
#         result = ""
#         for idx, val in enumerate(s):
#
#             if val in t:
#
#                 if val in dict:
#                     dict[val] = idx
#                 else:
#                     dict[val] = idx
#
#                 if sorted(str.join("", dict.keys())) == target:
#                     dict_values_ = s[min(dict.values()): max(dict.values())+1]
#                     if min_value > len(dict_values_):
#                         min_value = len(dict_values_)
#                         result = dict_values_
#
#         return result
#
#
# # Solution().minWindow("ADOBECODEBANC", "ABC")
