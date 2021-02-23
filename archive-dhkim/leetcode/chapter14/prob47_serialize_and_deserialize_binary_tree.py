
"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = [(1, root)]
        seq_val_tuples = []

        while queue:
            seq, node = queue.pop(0)

            seq_val_tuples.append(f"{seq}_{node.val}")

            if node.left:
                queue.append((seq * 2, node.left))
            if node.right:
                queue.append((seq * 2 + 1, node.right))

        return ",".join(seq_val_tuples)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        seq_val_tuples = data.split(",")

        f_seq, f_val = seq_val_tuples[0].split('_')

        root = TreeNode()
        parent = TreeNode(int(f_val))
        root.left = parent

        queue = [(1, parent)]

        for tup_str in seq_val_tuples[1:]:
            splited = tup_str.split('_')
            tmp_seq = int(splited[0])
            tmp_val = int(splited[1])

            tmp_node = TreeNode(tmp_val)

            while tmp_seq // 2 != queue[0][0]:
                queue.pop(0)

            if tmp_seq % 2 == 0:
                queue[0][1].left = tmp_node
            else:
                queue[0][1].right = tmp_node

            queue.append((tmp_seq, tmp_node))

        return root.left


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
