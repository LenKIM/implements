from typing import List

# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:

    def getTotalBinaryCode(self, __k: int) -> List:
        # 숫자만큼의 이진코드 생성
        max_value = ("1" * __k)
        # print(int(max_value, 2))
        get_bin = lambda x: format(x, 'b')
        _list = []
        for i in range(0, int(max_value, 2) + 1):
            _list.append(get_bin(i))
        return _list

    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = self.getTotalBinaryCode(k)
        print(codes)
        for idx, val in enumerate(s[:-k]):
            k_ = s[idx: idx + k]
            print(k_)
            if k_ in codes:
                codes.remove(k_)
            else:
                return False
        return True

    def hasAllCodes2(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()
        print(need)
        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False
if __name__ == '__main__':
    solution = Solution()
    code = solution.hasAllCodes2("00110110", k=2)
