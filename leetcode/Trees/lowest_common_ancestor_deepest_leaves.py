# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_d = 0
    lowest_leaves = []

    def lca(self, root, nodes):
        if root is None:
            return None
        if root in nodes:
            return root
        left = self.lca(root.left, nodes)
        right = self.lca(root.right, nodes)
        if left and right:
            return root

        if left is None and right is None:
            return None

        if left is None:
            return right

        return left

    def find_deepest_leaves(self, root, d):
        if root:
            if d > self.max_d:
                self.max_d = d
                self.lowest_leaves = []
                self.lowest_leaves.append(root)
            if d == self.max_d:
                self.lowest_leaves.append(root)
            self.find_deepest_leaves(root.left, d + 1)
            self.find_deepest_leaves(root.right, d + 1)

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.find_deepest_leaves(root, 0)
        return self.lca(root, self.lowest_leaves)
