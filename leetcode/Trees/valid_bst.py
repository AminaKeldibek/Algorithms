# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValidSub(node, cur_min, cur_max):
            if node:
                if node.val > cur_min and node.val < cur_max:
                    return isValidSub(node.left, cur_min, node.val) and
                           isValidSub(node.right, node.val, cur_max)
                return False
            return True
        return isValidSub(root, -float("inf"), float("inf"))
