from typing import List


class Solution:
    # nPn
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                elements_ = prev_elements[:] # Stack
                results.append(elements_)

            # 순열 생성 재귀 호출
            for e in elements: # 순서대로
                temp = elements[:]
                temp.remove(e)

# 위치를 찾아가서 지워
# temp - [1,2,3] | [2,3] | [3]   |  []  result.append    |  [3]       | [2,3] | [2]
# prev = []      | [1]   | [1,2] |  [1,2,3]              | popup [1,2]| [1]   | [1,3]
                prev_elements.append(e)
                dfs(temp)
                prev_elements.pop()







        return results


nums = [1, 2, 3]
permute = Solution().permute(nums)
print(permute)
