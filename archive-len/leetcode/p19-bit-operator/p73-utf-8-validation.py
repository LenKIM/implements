from typing import List

"""
https://leetcode.com/problems/utf-8-validation/

UTF-8 

UTF-8 구조?

1 > 0xxxxxxx
2 > 110xxxxx 10xxxxxx
3 > 1110xxxx 10xxxxxx 10xxxxxx
4 > 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

"""


class Solution:
    def check(self, _list, n):
        # 조건 충족안하면 True
        if len(_list) != n:
            return True

        for n in _list:
            if not format(n, '#010b').startswith("0b10"):
                return True
        return False

    def validUtf8(self, data: List[int]) -> bool:
        # offset 을 결정
        offset = 0
        size = len(data)
        while size > offset:

            current = format(data[offset], '#010b')
            if current.startswith("0b0"):
                start = offset
                offset = offset + 1
                if self.check(data[start+1:offset], 0):
                    return False

            elif current.startswith("0b110"):
                start = offset
                offset = offset + 2
                if self.check(data[start+1:offset], 1):
                    return False

            elif current.startswith("0b1110"):
                start = offset
                offset = offset + 3
                if self.check(data[start+1:offset], 2):
                    return False

            elif current.startswith("0b11110"):
                start = offset
                offset = offset + 4
                if self.check(data[start+1:offset], 3):
                    return False
            else:
                return False
        return True


utf_ = Solution().validUtf8([197, 130, 1])
# utf_ = Solution().validUtf8([235, 140, 4])
# utf_ = Solution().validUtf8([237])
# utf_ = Solution().validUtf8([228, 189, 160, 229, 165, 189, 13, 10])
# utf_ = Solution().validUtf8([115,100,102,231,154,132,13,10])
# utf_ = Solution().validUtf8([39,89,227,83,132,95,10,0])
print(utf_)
