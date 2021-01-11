from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                elements_ = prev_elements[:]
                results.append(elements_)

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)

                prev_elements.pop()

        dfs(nums)
        return results


nums = [1, 2, 3]
permute = Solution().permute(nums)
print(permute)
