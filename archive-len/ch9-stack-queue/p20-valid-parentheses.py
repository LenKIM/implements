# 괄호 입력값 올바른지 판별
# ()[]{}
# true

class Solution(object):

    def valid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0


solution = Solution()
solution.valid("()[]{}")
