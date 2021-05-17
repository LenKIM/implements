import heapq
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        # if g and s:
        #     heapq.heapify(g)
        #     heapq.heapify(s)
        #     g_val = heapq.heappop(g)
        #     s_val = heapq.heappop(s)
        #     while g and s:
        #         if g_val <= s_val:
        #             g_val = heapq.heappop(g)
        #             s_val = heapq.heappop(s)
        #             res += 1
        #         else :
        #             g_val = heapq.heappop(g)
        #
        #     if g_val <= s_val and ((g and not s) or (not g and s)):
        #         res += 1
        i, j = 0, 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i+=1
            j+=1
        return i

sol = Solution()
g = [7,8,9,10]
s = [5,6,7,8]
print(sol.findContentChildren(g,s))