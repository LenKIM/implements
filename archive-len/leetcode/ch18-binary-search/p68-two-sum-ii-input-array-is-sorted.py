from typing import List

'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

앞 문제와의 차이점은 정렬이 되어있냐? 안되어있냐?
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx, val in enumerate(numbers):
            left, right = idx + 1, len(numbers) - 1
            expected = target - val

            # 이진 탐색으로 나머지 값과 동일한 값 찾기. 없는 값은 없음.
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return [idx + 1, mid + 1]
