# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 문제 정의 - 트리에서 가장 긴 거리 찾기.
# 어떻게 풀 것인가?
# 가장 부모 노드에서 가장 말단 노드까지 가는데, 이때 오른쪽/왼쪽의 거리를 계산해서 sum 한다.


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest


solution = Solution()
node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

solution.diameterOfBinaryTree(node)

# 왜 2를 더했는가?
#
# 왜 1을 더했는가?
