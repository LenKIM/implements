from typing import List

"""
https://leetcode.com/problems/permutations
"""


class Solution01:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        results = []

        def DFS(stack):    
            for d in nums:
                if d not in stack:
                    DFS(stack + [d])

            if len(stack) == len(nums):
                results.append(stack)
                
        DFS([])
                
        return results
