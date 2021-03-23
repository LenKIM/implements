import collections
from typing import List


# 겹쳐진다면 합쳐라!
# 겹쳐짐을 어떻게 알 수 있을까?
# 1,3 | 2, 6

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        l = sorted(intervals, key=lambda x: x[0])

        # 하나씩 꺼내오면서 만약 이전값과 합쳐질 수 있다면 합치기
        q = [l[0]]
        for interval in l:

            # if q:
            temp = q[-1]
            if temp[0] <= interval[0] <= temp[1]:
                if temp[0] <= interval[1] <= temp[1]:
                    pass
                else:
                    temp = q.pop()
                    q.append([temp[0], interval[1]])
            else:
                q.append(interval)
        return q


# Solution().merge([[2,6],[1,3],[8,10],[9,18]])
Solution().merge([[2, 6], [1, 10], [8, 10], [9, 18]])
# Solution().merge([[1,4],[4,5]])

# result = []
# for item in sorted(intervals, key=lambda x: x[0]):
#     if result and item[0] <= result[-1][1]:
#         result[-1][1] = item[1] if item[1] > result[-1][1] else result[-1][1]
#     else:
#         result.append(item)
#
# print(result)
# return result
