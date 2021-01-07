import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = collections.Counter(nums)
        result = []
        for a in count:
            heapq.heappush(result, (-count[a], a))

        print(result)
        # print(result)
        topk = list()
        for _ in range(k):
            result_ = heapq.heappop(result)[1]  # [1]의 의미는 2번째 튜
            topk.append(result_)

        return result

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4]
k = 2

solution = Solution()
k_frequent = solution.topKFrequent(nums, k)
# print(k_frequent)
