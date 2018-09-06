class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def maxDepthHelper(node):
            max_depth = 0
            if node.children is None:
                return 1
            for child in node.children:
                max_depth = max(max_depth, maxDepthHelper(child))
            return 1 + max_depth

        if root is None:
            return 0

        return maxDepthHelper(root)
