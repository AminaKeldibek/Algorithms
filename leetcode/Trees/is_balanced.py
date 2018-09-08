class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack1 = [root]  # nodes
        stack2 = []  # values

        if root is None:
            return True

        while len(stack1) > 0:
            top = stack1.pop()
            stack2.append(top)

            if top.left is not None:
                stack1.append(top.left)
            if top.right is not None:
                stack1.append(top.right)

        for node in reversed(stack2):
            if node.left is not None and node.right is not None:
                node.depth = max(node.left.depth, node.right.depth) + 1
                if abs(node.left.depth - node.right.depth) > 1:
                    return False

            elif node.left is None and node.right is not None:
                node.depth = node.right.depth + 1
                if node.right.depth > 1:
                    return False

            elif node.right is None and node.left is not None:
                node.depth = node.left.depth + 1
                if node.left.depth > 1:
                    return False

            else:
                node.depth = 1

        return True
