"""
https://leetcode.com/problems/maximum-depth-of-binary-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0        
        
        bfs_queue = [root]
        maximum_depth = 0
        
        while bfs_queue:
            maximum_depth += 1            
            depth_len = len(bfs_queue)
            
            for _ in range(depth_len):
                node = bfs_queue.pop(0)
                
                if node and node.left:
                    bfs_queue.append(node.left)
                if node and node.right:
                    bfs_queue.append(node.right)
        
        return maximum_depth
            
        