# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.num_moves = 0

        def count_moves(node):
            if node is None:
                return 0
            left, right = count_moves(node.left), count_moves(node.right)
            self.num_moves += abs(left) + abs(right)

            return node.val + left + right - 1

        count_moves(root)

        return self.num_moves
        
