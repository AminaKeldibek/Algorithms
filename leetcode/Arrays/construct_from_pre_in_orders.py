# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        def buildTreeHelper(in_start_idx, in_end_idx):
            if in_start_idx > in_end_idx:
                return None
            node = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            if in_start_idx == in_end_idx:
                return node
            in_idx = searchIdx(inorder, node.val, in_start_idx, in_end_idx)
            node.left = buildTreeHelper(in_start_idx, in_idx - 1)
            node.right = buildTreeHelper(in_idx + 1, in_end_idx)
            return node

        def searchIdx(v, val, idx_start, idx_end):
            for i in xrange(idx_start, idx_end + 1):
                if v[i] == val:
                    return i

        self.pre_idx = 0

        return buildTreeHelper(0, len(inorder) - 1)
