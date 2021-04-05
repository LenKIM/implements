
"""
https://leetcode.com/problems/range-sum-of-bst
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        if not root:
            return 0

        def traverse(node) -> int:

            if not node:
                return 0

            node_val = node.val if low <= node.val <= high else 0

            # 불필요한 순회는 하지 않는다
            left_val = traverse(node.left) if low <= node.val else 0
            right_val = traverse(node.right) if node.val <= high else 0

            return node_val + left_val + right_val

        result = traverse(root)

        return result
