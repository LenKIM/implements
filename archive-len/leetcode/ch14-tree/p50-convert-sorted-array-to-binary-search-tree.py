# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 끝에 도달하면
        if not nums:
            return None

        # int
        mid = len(nums) // 2

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root