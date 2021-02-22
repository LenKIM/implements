# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:

        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root


node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
solution = Solution()
print(solution.bstToGst(node))
# def dfs(node: TreeNode, val):
# if not node:
#     return 0
#
# right_val = dfs(node.right, val)
#
# root_value = node.val + right_val
#
# left_val = dfs(node.left, root_value)
#
# return root_value + right_val + left_val