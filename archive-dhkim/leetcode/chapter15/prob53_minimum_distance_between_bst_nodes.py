
"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDiffInBST(self, root: TreeNode) -> int:

        seq = []
        minimums = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)

            if seq:
                minimums.append(node.val - seq[-1])

            seq.append(node.val)
            # print(f">> node.val : {node.val}, seq: {seq}")

            traverse(node.right)

        traverse(root)

        return min(minimums)
