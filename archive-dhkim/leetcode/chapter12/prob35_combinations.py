from typing import List

"""
https://leetcode.com/problems/combinations
"""


class Solution01:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        results = []
        data = [i+1 for i in range(n)]
        
        def DFS(stack, data, k):
            for i, d in enumerate(data):
                if d not in stack and len(stack) < k:
                    DFS(stack + [d], data[i+1:], k)

            if len(stack) == k:
                results.append(stack)
                
        DFS([], data, k)
                
        return results
