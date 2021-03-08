# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def makeTree(start: int, end: int, len):
            root = TreeNode(preorder[start])
            if(start == 0 and end == len-1):
                return root
            for i in range(start,end+1):
                if preorder[start] == inorder[i]:
                    #Left side
                    if start < i:
                        root.left = makeTree(start,i-1, len)
                    #Right side
                    if end > i :
                        root.right = makeTree(i+1,end, len)
                    break

            return root
        return makeTree(0, len(inorder)-1,len(inorder))
#         if inorder:
#             index = inorder.index(preorder.pop(0))
#
#             node = TreeNode(inorder[index])
#             node.left = self.buildTree(preorder,inorder[0:index])
#             node.right = self.buildTree(preorder,inorder[index+1:])
#
#             return node
