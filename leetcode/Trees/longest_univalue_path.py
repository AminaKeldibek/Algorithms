class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_score = 0

        def calcLongestPath(node):
            if node is None:
                return 0
            print node.val
            left_score = calcLongestPath(node.left)
            right_score = calcLongestPath(node.right)

            left_path = right_path = 0

            if node.left is not None and node.val == node.left.val:
                print "equal left"
                left_path = left_score + 1

            if node.right is not None and node.val == node.right.val:
                print "equal right"
                right_path = right_score + 1

            self.max_score = max(self.max_score, left_path + right_path)

            return max(left_path, right_path)

        calcLongestPath(root)
        return self.max_score
