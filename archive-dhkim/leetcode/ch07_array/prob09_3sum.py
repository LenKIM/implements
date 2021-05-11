from typing import List

"""
https://leetcode.com/problems/3sum
"""


class Solution:
    """
    세 수의 합이 0이 되는 조합들을 찾는 문제
    단순하게 brute force로 풀면 O(n^3)의 시간복잡도가 나오므로 타임오버가 된다.
    따라서 값들을 정렬하고 각 값에 대해서 대상 범위들을 투 포인터로 겹치지 않게 이동해가면 O(n^2)의 시간복잡도로 해결할 수 있다.
    -> 즉, 핵심은 투 포인터로 O(n^3)을 O(n^2)로 줄이는 것이다.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # 오름차순 정렬하여 포인터들의 합이 0보다 크거나 작으면 각 포인터를 이동시키며 답을 찾는다
        nums.sort()

        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            start = idx + 1
            end = len(nums) - 1
            target = 0 - nums[idx]

            # 현재 idx에 대해 조건을 만족하는 (start, end) 조합이 여러가지일 수 잇다.
            while start < end:
                if nums[start] + nums[end] < target:
                    start += 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    # 조건을 만족하는 start, end를 찾음 -> res 배열에 추가
                    local_res = [nums[idx], nums[start], nums[end]]
                    res.append(local_res)
                    print(local_res)

                    # 현재 start, end 포인터 외에도 조건을 만족하는 start, end가 더 있을 수 있으므로
                    # 값이 다른게 나올 때까지 start, end를 각각 앞/뒤로 전진시킨다
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    start += 1
                    while start < end and nums[end - 1] == nums[end]:
                        end -= 1
                    end -= 1

        return res
