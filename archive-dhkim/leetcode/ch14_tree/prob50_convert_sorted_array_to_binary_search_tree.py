from typing import List

"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def recursion(sub_nums):
            if len(sub_nums) == 1:
                return TreeNode(sub_nums[0])

            if len(sub_nums) == 0:
                return None

            middle_idx = len(sub_nums) // 2
            now_root = TreeNode(sub_nums[middle_idx])

            left_node = recursion(sub_nums[:middle_idx])
            now_root.left = left_node

            right_node = recursion(sub_nums[middle_idx + 1:])
            now_root.right = right_node

            return now_root

        root = recursion(nums)

        return root


if __name__ == "__main__":

    nums = [-10, -3, 0, 5, 9]   # output : [0,-3,9,-10,null,5] or [0,-10,5,null,-3,null,9]

    solution = Solution()
    res = solution.sortedArrayToBST(nums)
    print(res)
