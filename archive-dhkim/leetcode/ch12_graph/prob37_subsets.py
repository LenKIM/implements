from typing import List

"""
https://leetcode.com/problems/subsets
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:  
        
        results = []
        
        def dfs(ary, subset):            
            results.append(subset)            
            for idx, n in enumerate(ary):
                dfs(ary[idx+1:], subset + [n])
                
        dfs(nums, [])
                
        return results
