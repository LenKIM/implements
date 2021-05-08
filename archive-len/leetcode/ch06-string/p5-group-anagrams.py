import collections
from typing import List
"""
https://leetcode.com/problems/group-anagrams/

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

"""
input = ["eat", "tea", "tan", "ate", "nat", "bat"]


# 정렬하여 딕셔너리에 추가
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬해서 딕셔너리 추가
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()


if __name__ == '__main__':
    print(groupAnagrams(strs=input))
    # 그 외 여러가지 정렬 방법

    a = [2, 5, 1, 9, 7]
    l = sorted(a)
    print(l)

    b = 'zbdaf'
    "".join(sorted(b))  # 다시 문자열로 결합

    # 함수 길이로 정렬할 수 있음
    c = ['ccc', 'aaaa', 'd', 'bb']
    print(sorted(c, key=len))

    # 함수를 이용해 키를 정의하는 방법
    d = ['cde', 'cfc', 'abc']


    def fn(s):
        return s[0], s[-1]


    print(sorted(d, key=lambda s: (s[0], s[-1])))
