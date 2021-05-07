import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        chars = collections.Counter(tasks)
        while True:
            size = len(chars)
            sub = 0
            for char, cnt in chars.most_common(n+1):
                sub+=1
                result+=1
                chars.subtract(char)
                chars += collections.Counter()

            if not chars:
                break

            result += n - sub + 1
        return result
        #size = len(tasks)
        # char_nums = [0]*(ord('Z')-ord('A')+1)
        # chars = []
        # c_size  = 0
        # q = []
        # for c in tasks:
        #     if char_nums[ord(c)-ord('A')]==0:
        #         chars.append(c)
        #     char_nums[ord(c)-ord('A')]+=1
        # c_size = len(chars)
        #
        # while size>0:
        #     for i in range(n):
        #         if char_nums[ord(chars[i]) - ord('A')] > 0:
        #             q.append(chars[i])
        #             char_nums[ord(chars[i]) - ord('A')] -=1
        #             size -=1
        #         else :
        #             q.append("idle")

solution = Solution()
temp = ["A","A","A","B","B","B"]
print(solution.leastInterval(temp,2))