from typing import List

"""
https://leetcode.com/problems/number-of-islands
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            grid[i][j] = "-1"

            directions = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]    
            for di, dj in directions:
                if 0 <= di < len(grid) and 0 <= dj < len(grid[i]) and grid[di][dj] == "1":
                    dfs(di, dj)


        island_cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island_cnt += 1
                    
        return island_cnt
