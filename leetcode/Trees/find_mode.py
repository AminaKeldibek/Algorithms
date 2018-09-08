class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def countUnique(node, d):
            if node is not None:
                if node.val in d:
                    d[node.val] += 1
                else:
                    d[node.val] = 1
                countUnique(node.left, d)
                countUnique(node.right, d)

            return d

        if root is None:
            return []

        d = dict()
        d = countUnique(root, d)

        max_count = max(d.values())
        return [key for key, val in d.iteritems() if val == max_count]

    def findModeConstSpace(self, root):
        def inOrder(node):
            if node:
                for n in inOrder(node.left):
                    yield n
                yield node.val
                for n in inOrder(node.right):
                    yield n
        prev = None
        max_freq = 1
        freq = 1
        for node in inOrder(root):
            if node == prev:
                freq += 1
                max_freq = max(max_freq, freq)
            else:
                freq = 1
            prev = node

        freq = 1
        prev = None
        modes = set()
        for node in inOrder(root):
            if node == prev:
                freq += 1
            else:
                freq = 1
            if freq == max_freq:
                modes.add(node)
            prev = node

        return modes
