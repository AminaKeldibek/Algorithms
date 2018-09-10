# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def getRoot(nums):
            root_val = max(nums)
            root_idx = nums.index(root_val)
            root = TreeNode(root_val)
            if root_idx > 0:
                root.left = getRoot(nums[0:root_idx])
            if root_idx < len(nums) - 1:
                root.right = getRoot(nums[root_idx + 1:len(nums)])
            return root

        if len(nums) == 0:
            return None

        return getRoot(nums)
