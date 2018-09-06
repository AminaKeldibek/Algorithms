# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left, right):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getLeafSeq(node, leaves):
            if node is not None:
                if node.left is None and node.right is None:
                    leaves.append(node.val)
                getLeafSeq(node.left, leaves)
                getLeafSeq(node.right, leaves)

        leaves1 = []
        leaves2 = []
        getLeafSeq(root1, leaves1)
        getLeafSeq(root2, leaves2)

        return leaves1 == leaves2
