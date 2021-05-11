from typing import List

"""
https://leetcode.com/problems/utf-8-validation
"""


class Solution:
    """
    입력값들을 이진수 바이트로 나타냈을 때, 각 바이트의 첫 ?개 비트값의 패턴에 따라 다음 ?개 바이트 패턴이 정해짐
    이러한 규칙들을 만족하는지 검사하는 문제
    """
    def validUtf8(self, data: List[int]) -> bool:

        def is_valid_remains(ary, idx_gte, idx_lt):
            if idx_lt > len(ary):
                return False

            for n in ary[idx_gte: idx_lt]:
                if (n >> 6) != 0b10:
                    return False

            return True

        idx = 0
        while idx < len(data):
            now_data = data[idx]

            if (now_data >> 7) == 0:
                idx += 1
            elif (now_data >> 5) == 0b110 and is_valid_remains(data, idx + 1, idx + 2):
                idx += 2
            elif (now_data >> 4) == 0b1110 and is_valid_remains(data, idx + 1, idx + 3):
                idx += 3
            elif (now_data >> 3) == 0b11110 and is_valid_remains(data, idx + 1, idx + 4):
                idx += 4
            else:
                return False

        return True
