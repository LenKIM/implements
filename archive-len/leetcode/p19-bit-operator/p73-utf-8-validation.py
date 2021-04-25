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
    def validUtf8(self, data: List[int]) -> bool:
        first = format(data[0], '#010b')

        if first.startswith('0b0'):
            # 모든 값들이

            if len(data) == 1:
                value = data[0]
                if format(value, '#010b')[2:4] == '10':
                    return False
            else:
                return False

            return True

        elif first.startswith('0b110'):
            fixed_bytes = data[1:2]
            if len(data) >= 2:
                rest_byte = data[2]
            else:
                rest_byte = 0


            if len(fixed_bytes) < 1:
                return False

            for fixed_byte in fixed_bytes:
                if format(fixed_byte, '#010b')[2:4] != '10':
                    return False

            if format(rest_byte, '#010b')[2:4] == '10':
                return False

            return True
        elif first.startswith('0b1110'):

            fixed_bytes = data[1:3]
            if len(data) >= 4:
                rest_byte = data[3]
            else:
                rest_byte = 0

            if len(fixed_bytes) < 2:
                return False

            for fixed_byte in fixed_bytes:
                if format(fixed_byte, '#010b')[2:4] != '10':
                    return False

            if format(rest_byte, '#010b')[2:4] == '10':
                return False
            return True
        elif first.startswith('0b11110'):
            fixed_bytes = data[1:4]
            if len(data) >= 5:
                rest_byte = data[4]
            else:
                rest_byte = 0

            if len(fixed_bytes) < 3:
                return False

            for fixed_byte in fixed_bytes:
                if format(fixed_byte, '#010b')[2:4] != '10':
                    return False

            if format(rest_byte, '#010b')[2:4] == '10':
                return False
            return True
        else:
            return False



# utf_ = Solution().validUtf8([197, 130, 1])
# utf_ = Solution().validUtf8([235, 140, 4])
# utf_ = Solution().validUtf8([10])
# utf_ = Solution().validUtf8([228,189,160,229,165,189,13,10])
utf_ = Solution().validUtf8([115,100,102,231,154,132,13,10])
# utf_ = Solution().validUtf8([39,89,227,83,132,95,10,0])
print(utf_)


