# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res=0
        Q=[(root, 0)]
        while(Q):
            res=max(res, 1 if len(Q)==1 else Q[-1][1]-Q[0][1]+1)
            new=[]
            for q in Q:
                if q[0].left:
                    new.append((q[0].left, 2*q[1]))
                if q[0].right:
                    new.append((q[0].right, 2*q[1]+1))
            Q=new
        return res
