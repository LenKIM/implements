from typing import List


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         row_start = 0
#         row_end = len(matrix[0])
#         col_start = 0
#         col_end = len(matrix)
#
#         while row_start < row_end:
#             row_mid = row_start - (row_start - row_end) // 2
#             if matrix[row_mid][0]>target:
#                 row_end = row_mid-1
#             elif matrix[row_mid][0]<target:
#                 col_start = 0
#                 col_end = len(matrix)
#                 while col_start < col_end:
#                     col_mid = col_start - (col_start - col_end)//2
#                     if matrix[row_mid][col_mid]>target:
#                         col_end = col_mid-1
#                     elif matrix[row_mid][col_mid]<target:
#                         col_start = col_mid+1
#                     else:
#                         True
#                 row_start = row_mid + 1
#             else:
#                 return True
#         return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)