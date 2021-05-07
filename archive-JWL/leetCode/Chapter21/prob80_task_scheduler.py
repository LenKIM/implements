import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = collections.Counter(tasks).most_common(n+1)
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


        print(q)
        return 0
solution = Solution()
temp = ["A","A","A","B","B","B","C","C","C"]
solution.leastInterval(temp,10)