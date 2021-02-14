# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
#       (using stack)
        
        # if(root is None):
        #     return 
        # s=[root] 
        # while(s):
        #     curr=s.pop()
        #     if(curr.right):
        #         s.append(curr.right)
        #     if(curr.left):
        #         s.append(curr.left)
        #     if(s):
        #         curr.right=s[-1]
        #     curr.left=None
        
        # if(root is None or root.left is None and root.right is None):
        #     return
        # if(root.left):
        #     self.flatten(root.left)
        #     temp=root.right
        #     root.right=root.left
        #     root.left=None
        #     curr=root.right
        #     while(curr.right):
        #         curr=curr.right
        #     curr.right=temp
        # self.flatten(root.right)
        
        curr=root
        while curr:
            if curr.left:
                pre=curr.left
                while pre.right:
                    pre=pre.right
                pre.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right
