# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def calculateMaxPath(node):
            nonlocal max_sum
            if(node is None):
                return 0
            left = max(calculateMaxPath(node.left), 0)
            right = max(calculateMaxPath(node.right), 0)
            max_sum = max(left + right + node.val, max_sum)
            return max(left, right) + node.val
        max_sum = float('-inf')
        calculateMaxPath(root)
        return max_sum
        
    
