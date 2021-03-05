# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    v_list = []

    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node.val:
                self.v_list.append(node.val)
                dfs(node.right)
                dfs(node.left)
            return node

        dfs(root)
        self.v_list.sort()
        upper = self.v_list[1:]
        behind = self.v_list[:-1]


        mx = sys.maxsize
        for i, j in zip(upper, behind):
            mx = min(mx, i - j)

        return mx


node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
solution = Solution()
print(solution.minDiffInBST(node))
