# 중앙을 기준으로 이진 트리를 반전하는 문제

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                print(node.val)


            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root
        # if root:
        #     root.left, root.right = \
        #         self.invertTree(root.right), self.invertTree(root.left)
        #
        #     return root
        #
        # return None

node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
solution = Solution()
solution.invertTree(node)
