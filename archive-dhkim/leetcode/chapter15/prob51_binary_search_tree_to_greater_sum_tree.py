
"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        desc_nums = []

        def traverse(node):
            if node is None:
                return

            traverse(node.right)

            desc_nums.append(node.val)
            node.val = sum(desc_nums)

            traverse(node.left)

        traverse(root)

        return root
