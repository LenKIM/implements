
"""
https://leetcode.com/problems/jewels-and-stones
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        counter = dict()
        for s in S:
            if s in counter:
                counter[s] += 1
            else:
                counter[s] = 1

        result = 0

        for j in J:
            if j in counter:
                result += counter[j]

        return result
