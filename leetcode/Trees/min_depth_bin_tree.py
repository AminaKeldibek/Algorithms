class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findMinDepth(node):
            if node is None:
                return 0

            left_depth = findMinDepth(node.left)
            right_depth = findMinDepth(node.right)
            if node.left is not None and node.right is not None:
                return min(left_depth, right_depth) + 1
            elif node.left is None:
                return right_depth + 1
            else:
                return left_depth + 1

        return findMinDepth(root)
