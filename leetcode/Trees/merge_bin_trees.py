# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def mergeTreesHelper(t1, t2):
            if t1 is None:
                return t2
            if t2 is None:
                return t1

            t1.val = t1.val + t2.val
            t1.right = mergeTreesHelper(t1.right, t2.right)
            t1.left = mergeTreesHelper(t1.left, t2.left)

            return t1

        return mergeTreesHelper(t1, t2)
