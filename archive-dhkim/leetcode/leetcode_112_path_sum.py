
"""
https://leetcode.com/problems/path-sum/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if root is None:
            return False

        if root.left is None and root.right is None:
            if sum == root.val:
                return True
            else:
                return False

        if self.hasPathSum(root.left, sum - root.val):
            return True
        elif self.hasPathSum(root.right, sum - root.val):
            return True
        else:
            return False


