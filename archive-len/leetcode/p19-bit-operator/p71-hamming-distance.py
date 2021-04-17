'''
 두 정수를 입력받아 몇 비트가 다른지 계산하기
 https://leetcode.com/problems/hamming-distance/
'''


class Solution:

    def hammingDistance(self, x: int, y: int) -> int:
        s = bin(x ^ y)
        return s.count('1')


distance = Solution().hammingDistance(1, 4)
