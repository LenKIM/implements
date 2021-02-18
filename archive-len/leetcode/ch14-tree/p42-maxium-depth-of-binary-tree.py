import collections


class TreeNode(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode):
        ...
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.left:
                    queue.append(cur_root.right)
            # BFS 반복 횟수 == 깊
        return depth
