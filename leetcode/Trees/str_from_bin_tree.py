# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.PreOrder2Str(t)


    def PreOrder2Str(self, node):
        s = ''
        if node:
            s = str(node.val)
            if node.right:
                s += '(' + self.PreOrder2Str(node.left) + ')'
                s += '(' + self.PreOrder2Str(node.right) + ')'
            elif node.left:
                s += '(' + self.PreOrder2Str(node.left) + ')'
        return s
