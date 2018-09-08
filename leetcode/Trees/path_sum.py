class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        root.sum = sum
        stack = [root]

        while len(stack) > 0:
            top = stack.pop()
            rem = top.sum - top.val
            if not top.left and not top.right and rem == 0:
                return True
            else:
                if top.left:
                    top.left.sum = rem
                    stack.append(top.left)
                if top.right:
                    top.right.sum = rem
                    stack.append(top.right)

        return False
