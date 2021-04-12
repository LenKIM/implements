
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

    def invertTree_another(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return None

            left_child = dfs(node.left)
            right_child = dfs(node.right)

            node.left = right_child
            node.right = left_child

            return node

        return dfs(root)
