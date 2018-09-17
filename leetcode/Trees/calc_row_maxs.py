# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        row_maxs = [root.val]
        q1 = deque([root])
        q2 = deque([])

        while len(q1) > 0:
            front = q1.popleft()

            if front.left:
                q2.append(front.left)
            if front.right:
                q2.append(front.right)

            if len(q1) == 0 and len(q2) > 0:
                row_maxs.append(max([node.val for node in q2]))
                while len(q2) > 0:
                    q1.append(q2.popleft())

        return row_maxs
