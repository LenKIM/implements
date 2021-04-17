from typing import List

'''

https://leetcode.com/problems/search-a-2d-matrix-ii/

'''


class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # return any(target in x for x in matrix)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row, col = 0, len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col = col - 1
            elif matrix[row][col] < target:
                row = row + 1

        return False