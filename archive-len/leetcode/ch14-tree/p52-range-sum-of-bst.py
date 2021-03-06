# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    low_value = 0
    high_value = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        valid_list = []
        def dfs(root: TreeNode):
            if root:
                value = root.val
                if low <= value <= high:
                    valid_list.append(value)
                dfs(root.right)
                dfs(root.left)
            return root

        dfs(root)
        return sum(valid_list)


node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
solution = Solution()
print(solution.rangeSumBST(node, 2, 5))
