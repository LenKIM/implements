from typing import List

"""
https://leetcode.com/problems/combination-sum
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
                
        results = []
        
        def dfs(cand_list, buffer):
            
            cand_sum = sum(buffer)
            
            if cand_sum == target:
                results.append(buffer)
                return
            elif cand_sum > target:
                return
                
            for idx, cand in enumerate(cand_list):
                dfs(cand_list[idx:], buffer + [cand])
                
        dfs(candidates, [])
        
        return results
