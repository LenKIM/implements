import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode):
        def dfs(_root: TreeNode, level):
            if not _root:
                return 0

            right_chain = dfs(_root.right, level)
            left_chain = dfs(_root.left, level)

            max_depth = max(right_chain, left_chain) + 1
            return max_depth

        return dfs(root, 1)


node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
solution = Solution()
depth = solution.maxDepth(node)
print(depth)

# queue = collections.deque([root])
# depth = 0
#
# while queue:
#     depth += 1
#     for _ in range(len(queue)):
#         cur_root = queue.popleft()
#         if cur_root.left:
#             queue.append(cur_root.left)
#         if cur_root.left:
#             queue.append(cur_root.right)
# # BFS 반복 횟수 == 깊이
# return depth
