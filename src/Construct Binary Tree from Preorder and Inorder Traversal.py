# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         return self.helper(0,0,len(inorder)-1,preorder,inorder)
    
#     def helper(self,pre_start,in_start,in_end,preorder,inorder):
#         if pre_start>len(preorder)-1 or in_start>in_end:
#             return None
#         root = TreeNode(preorder[pre_start])
#         in_idx = inorder.index(root.val)
#         root.left = self.helper(pre_start+1,in_start,in_idx-1,preorder,inorder)
#         root.right = self.helper(pre_start+in_idx-in_start+1,in_idx+1,in_end,preorder,inorder)
#         return root
        
        if not preorder: return None
        node = root = TreeNode(preorder[0])
        stack = []
        pos = {} 
        for i in range(len(inorder)):
            pos[inorder[i]]=i
        for val in preorder[1:]: 
            if pos[val] < pos[node.val]: 
                node.left = TreeNode(val)
                stack.append(node)
                node = node.left 
            else: 
                while stack and pos[val] > pos[stack[-1].val]: node = stack.pop()
                node.right = TreeNode(val)
                node = node.right 
        return root 
