
"""
https://leetcode.com/problems/diameter-of-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameters = []

        def dfs(node):
            if not node:
                return []

            left_chain = dfs(node.left)
            right_chain = dfs(node.right)

            diameter = left_chain + right_chain
            diameters.append(len(diameter))

            if len(left_chain) > len(right_chain):
                return left_chain + [node.val]
            else:
                return right_chain + [node.val]

        dfs(root)
        
        if diameters:
            return max(diameters)
        else:
            return 0
