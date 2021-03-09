from typing import List

"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 1. preorder 맨 앞 값이 root임
        root_val = preorder.pop(0)

        # 2. inorder를 root_val 기준으로 좌우 서브트리로 나눔
        in_root_idx = inorder.index(root_val)
        in_sub_left = inorder[:in_root_idx]
        in_sub_right = inorder[in_root_idx+1:]

        # 3. inorder 좌우 서브트리 사이즈만큼 preorder의 root 이후 부분을 좌우 서브트리로 나눔
        pre_sub_left = preorder[:len(in_sub_left)]
        pre_sub_right = preorder[len(in_sub_left):]

        # 4. 각 좌우 inorder, preorder 서브트리에 대해 본 함수를 재귀 수행
        left_sub_root = self.buildTree(pre_sub_left, in_sub_left) if pre_sub_left else None
        right_sub_root = self.buildTree(pre_sub_right, in_sub_right) if pre_sub_right else None

        # 5. 양 서브트리의 루트 노드를 현재 루트노드의 좌우 자식노드로 연결
        root = TreeNode(root_val)
        root.left = left_sub_root
        root.right = right_sub_root

        # 6. 자식 연결된 현재 루트노드를 반환
        return root

    def inorder_traverse(self, node):
        """ test """
        if node:
            self.inorder_traverse(node.left)
            print(node.val)
            self.inorder_traverse(node.right)

    def preorder_traverse(self, node):
        """ test """
        if node:
            print(node.val)
            self.preorder_traverse(node.left)
            self.preorder_traverse(node.right)


if __name__ == "__main__":
    """
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
    """

    solution = Solution()
    res = solution.buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7])

    print('>> inorder')
    solution.inorder_traverse(res)

    print('>> preorder')
    solution.preorder_traverse(res)







