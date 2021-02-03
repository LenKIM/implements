
"""
https://leetcode.com/problems/longest-univalue-path
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0
    
    def longestUnivaluePath(self, node: TreeNode):
        
        def dfs(tmp, parent_val):
            
            if tmp is None:
                return 0
            
            left_length = dfs(tmp.left, tmp.val)
            right_length = dfs(tmp.right, tmp.val)
            
            self.result = max(self.result, left_length + right_length)
            
            if tmp.val == parent_val:
                return max(left_length, right_length) + 1
            else:
                return 0
            
        dfs(node, 0)
        
        return self.result
