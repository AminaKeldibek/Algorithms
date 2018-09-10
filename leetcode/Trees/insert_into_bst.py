# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def setChild(node, child_node):
            if child_node > node.val:
                if node.right is None:
                    node.right = TreeNode(child_node)
                else:
                    setChild(node.right, child_node)
            else:
                if node.left is None:
                    node.left = TreeNode(child_node)
                else:
                    setChild(node.left, child_node)

        setChild(root, val)
        return root
