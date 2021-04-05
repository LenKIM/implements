
"""
https://leetcode.com/problems/merge-two-binary-trees
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return None

            val1 = node1.val if node1 is not None else 0
            val2 = node2.val if node2 is not None else 0
            merge_node = TreeNode(val1 + val2)

            left_node = dfs(node1.left if node1 else None, node2.left if node2 else None)
            right_node = dfs(node1.right if node1 else None, node2.right if node2 else None)
            merge_node.left = left_node
            merge_node.right = right_node

            return merge_node

        return dfs(root1, root2)
