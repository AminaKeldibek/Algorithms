# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def PreOrder(node):
            if node:
                s = str(node.val)
                s += "," + PreOrder(node.left)
                s += "," + PreOrder(node.right)
            else:
                s = "None"
            return s

        return PreOrder(root)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_iter = iter(data.split(','))

        def PreOrder():
            val = next(data_iter)
            if val != "None":
                print val
                node = TreeNode(int(val))
                node.left = PreOrder()
                node.right = PreOrder()
            else:
                node = None
            return node

        root = PreOrder()
        return root
