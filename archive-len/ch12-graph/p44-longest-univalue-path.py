# 동일한 값을 지닌 가장 긴 경로 찾기

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.longest = max(self.longest, left + right)
            return max(left, right)

        dfs(root)
        return self.longest
