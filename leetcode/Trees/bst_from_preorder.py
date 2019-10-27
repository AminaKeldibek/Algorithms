# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        root = TreeNode(preorder[0])
        main_root = root
        stack = [root]

        for cur_val in preorder[1:]:
            if cur_val < stack[-1].val:
                root.left = TreeNode(cur_val)
                stack.append(root.left)
                root = root.left
            else:
                while len(stack) > 0 and cur_val > stack[-1].val:
                    root = stack.pop()
                root.right = TreeNode(cur_val)
                stack.append(root.right)
                root = root.right

        return main_root
