#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if not root.left and root.right:
            return root.val

        max_depth = 1
        stack_nodes = [root]
        stack_depths = [1]

        while len(stack_nodes) > 0:
            top_node = stack_nodes.pop()
            top_depth = stack_depths.pop()

            if top_node.left:
                stack_nodes.append(top_node.left)
                stack_depths.append(top_depth + 1)
                max_depth = max(max_depth, top_depth + 1)
            if top_node.right:
                stack_nodes.append(top_node.right)
                stack_depths.append(top_depth + 1)
                max_depth = max(max_depth, top_depth + 1)

        stack_nodes = [root]
        stack_depths = [1]

        while len(stack_nodes) > 0:
            top_node = stack_nodes.pop()
            top_depth = stack_depths.pop()

            if top_node.left:
                stack_nodes.append(top_node.left)
                stack_depths.append(top_depth + 1)
                if top_depth + 1 == max_depth:
                    return top_node.left.val
            if top_node.right:
                stack_nodes.append(top_node.right)
                stack_depths.append(top_depth + 1)
                if top_depth + 1 == max_depth:
                    return top_node.right.val


def InOrder(node):
    if node is not None:
        for n in InOrder(node.left):
            yield n
        yield node.val
        for n in InOrder(node.right):
            yield n


def main():
    leaf1 = TreeNode(5)
    leaf2 = TreeNode(4)
    node2 = TreeNode(0, None, leaf2)
    root = TreeNode(1, None, node2)

    print Solution().findBottomLeftValue(root)


if __name__ == "__main__":
    main()
