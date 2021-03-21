from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for item in sorted (intervals, key=lambda x: x[0]):
            if result and item[0] <= result[-1][1]:
                result[-1][1] = item[1] if item[1]> result[-1][1] else result[-1][1]
            else:
                result.append(item)
        return result

        # length = len(intervals)
        # sorted(intervals, key=lambda x: x[0])
        #
        # for i in range(0, length - 1):
        #     print("i : ", i)
        #     for j in range(i + 1, length):
        #         print("j : ", j)
        #         if (intervals[i][1] > intervals[j][0]):
        #             intervals[i][1] = intervals[j][1] if intervals[i][1] < intervals[j][1] else intervals[i][1]
        #             del intervals[j]
        #             print(intervals)
        #             length = len(intervals)
        #         j -= 1
        #
        # return intervals


lists = [[1, 3], [2, 6], [8, 10], [15, 18]]
Solution.merge(lists)
