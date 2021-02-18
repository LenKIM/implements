# Definition for a binary tree node.
import collections


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

        deque = collections.deque([root])

        result = ['#']

        while deque:

            node = deque.popleft()

            if node:
                deque.append(node.left)
                deque.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data == "# #":
            return None

        lists = data.split(' ')

        idx = 2
        root = TreeNode(int(lists[1]))
        queue = collections.deque([root])
        while queue:

            node = queue.popleft()
            if lists[idx] != '#':
                node.left = TreeNode(int(lists[idx]))
                queue.append(node.left)
            idx += 1

            if lists[idx] != '#':
                node.right = TreeNode(int(lists[idx]))
                queue.append(node.right)
            idx += 1

        return root




    # Your Codec object will be instantiated and called as such:


codec = Codec()
# node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
# TreeNode(1)
#
# ser = codec.serialize(node)
# print(ser)
deser = codec.deserialize(['#',4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2])
print(deser)
# ans = deser.deserialize(ser.serialize(root))
