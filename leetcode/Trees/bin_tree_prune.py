#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def pruneHelper(node):
            if node is not None:
                node.left = pruneHelper(node.left)
                node.right = pruneHelper(node.right)
                if node.val == 0 and not (node.right and node.left):
                    return None
            return node
        print [node for node in InOrder(root)]
        pruneHelper(root)
        print [node for node in InOrder(root)]
        return root


def InOrder(node):
    if node is not None:
        for n in InOrder(node.left):
            yield n
        yield node.val
        for n in InOrder(node.right):
            yield n


def main():
    leaf1 = TreeNode(0)
    leaf2 = TreeNode(1)
    node2 = TreeNode(0, leaf1, leaf2)
    root = TreeNode(1, None, node2)

    for node in InOrder(root):
        print node
    Solution().pruneTree(root)


if __name__ == "__main__":
    main()
