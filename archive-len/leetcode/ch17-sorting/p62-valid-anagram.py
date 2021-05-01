'''
1. 해시
2. 정렬후 비교
'''
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = []
        for value in t:
            map.append(value)

        for val in s:
            if map.__contains__(val):
                map.remove(val)
            else:
                return False

        return len(map) == 0



print(Solution().isAnagram("aaaaaabbbbbb", "aabb"))