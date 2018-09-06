class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        x = root

        while not x is None and x.val != val:
            if val <= x.val:
                x = x.left
            else:
                x = x.right

        return x
