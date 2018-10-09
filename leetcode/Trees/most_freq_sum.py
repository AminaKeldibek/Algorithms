# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        d = defaultdict(int)
        def calcSubSum(node):
            if node is None:
                return 0
            sub_sum = node.val + calcSubSum(node.left) + calcSubSum(node.right)
            d[sub_sum] += 1

            return sub_sum

        calcSubSum(root)
        max_freq = max(d.values())
        return [k for k, v in d.iteritems() if v == max_freq]
        
