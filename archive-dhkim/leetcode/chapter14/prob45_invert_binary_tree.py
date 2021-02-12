
"""
https://leetcode.com/problems/invert-binary-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            dfs(node.right)

            tmp = node.left
            node.left = node.right
            node.right = tmp

        dfs(root)

        return root
