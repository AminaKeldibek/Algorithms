# Definition for a Node.
class Node(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def postorderRecursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def postorderHelper(node, nodes):
            if node is not None:
                if node.children is not None:
                    for child in node.children:
                        postorderHelper(child, nodes)
                nodes.append(node.val)

        nodes = []
        postorderHelper(root, nodes)

        return nodes

    def postorderIterative(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack1 = [root]  # nodes
        stack2 = []  # values

        while len(stack1) > 0:
            top = stack1.pop()
            stack2.append(top.val)

            if top.children is not None:
                for child in top.children:
                    stack1.append(child)

        return [i for i in reversed(stack2)]


def main():
    node5 = Node(5)
    node6 = Node(6)
    node2 = Node(2)
    node4 = Node(4)
    node7 = Node(7)
    node8 = Node(8)
    node3 = Node(3, [node5, node6])
    node4 = Node(4, [node7, node8])
    node1 = Node(1, [node3, node2, node4])

    print Solution().postorderRecursive(node1)
    print Solution().postorderIterative(node1)


if __name__ == '__main__':
    main()
