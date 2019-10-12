"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def preorder(self, root: 'Node') -> 'List[int]':
        if root is None:
            return []

        preorder_list = [root.val]
        stack = deque([root])
        hash_visited = {root: 1}

        while len(stack) > 0:
            top = stack.pop()
            if top.children:
                for child in top.children:
                    if child not in hash_visited:
                        hash_visited[child] = 1
                        preorder_list.append(child.val)
                        stack.append(top)
                        stack.append(child)
                        break

        return preorder_list
