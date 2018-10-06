from collections import defaultdict, Counter


class Solution(object):
    def findDuplicateSubtrees(self, root):
        trees = defaultdict()
        trees.default_factory = trees.__len__

        count = Counter()
        res = []

        def lookup(node):
            if node:
                tree_id = trees[node.val, lookup(node.left), lookup(node.right)]
                count[tree_id] += 1
                if count[tree_id] == 2:
                    res.append(node)
                return tree_id
        lookup(root)

        return res
