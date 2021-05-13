from typing import List

"""
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

s가 내가 가진 쿠키 개수
g가 아이들이 원하는 쿠키개수

"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        child_i = cookie_j = 0

        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i


# [10,9,8,7]
# [5,6,7,8]
children = Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8])
print(children)
