# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        map = dict()

        def calcMaxSum(node):
            if node is None:
                return 0
            if node not in map:
                grandchildren_sum = 0
                if node.left:
                    grandchildren_sum += calcMaxSum(node.left.left) + calcMaxSum(node.left.right)
                if node.right:
                    grandchildren_sum += calcMaxSum(node.right.left) + calcMaxSum(node.right.right)
                children_sum = calcMaxSum(node.right) + calcMaxSum(node.left)

                map[node] = max(node.val + grandchildren_sum, children_sum)

            return map[node]

        return calcMaxSum(root)
