# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            if node:
                if not visited:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                else:
                    if node.left and node.left.val == -1:
                        node.left = None
                    if node.right and node.right.val == -1:
                        node.right = None
                    if not node.left and not node.right:
                        if node.val == 0:
                            node.val = -1

        return root
