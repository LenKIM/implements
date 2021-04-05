
"""
https://leetcode.com/problems/balanced-binary-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_height_diff = 0

    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node):

            if node is None:
                return 0

            left_height = dfs(node.left) + 1
            right_height = dfs(node.right) + 1

            abs_diff = abs(left_height - right_height)
            self.max_height_diff = max(self.max_height_diff, abs_diff)

            return max(left_height, right_height)

        dfs(root)

        if self.max_height_diff > 1:
            return False
        else:
            return True
