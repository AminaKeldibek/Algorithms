class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def pruneHelper(node):
            if node is None:
                return False
            res_left = pruneHelper(node.left)
            res_right = pruneHelper(node.right)
            if not res_left:
                node.left = None
            if not res_right:
                node.right = None

            return node.val == 1 or res_left or res_right

        pruneHelper(root)
        return root
