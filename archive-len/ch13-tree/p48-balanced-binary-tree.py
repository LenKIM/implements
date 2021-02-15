# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root: TreeNode) -> int:

            if not root or None:
                return 0

            right_depth = dfs(root.right)
            left_depth = dfs(root.left)

            if abs(right_depth - left_depth) > 1 or \
                    right_depth == -1 or \
                    left_depth == -1:
                return -1

            return max(right_depth, left_depth) + 1

        return dfs(root) != -1


solution = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
solution.isBalanced(root)