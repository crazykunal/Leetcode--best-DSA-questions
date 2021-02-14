# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.ans = []
        self.count = 0
        self.max1 = 0
        self.pre = TreeNode(float('inf'))
        def inorder(root):
            if not root: return
            inorder(root.left)
            if self.pre.val == root.val:
                self.count += 1
            else:
                self.count = 1 
            if self.count > self.max1:
                self.max1 = self.count
                self.ans = [root.val]
            elif self.count == self.max1:
                self.ans.append(root.val)
            self.pre = root
            inorder(root.right)
        inorder(root)
        return self.ans
        
        # res, stack = [], []
        # ans, curr_count = 0,1
        # preVal = float('-inf')
        # while True:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     if not stack:
        #         return res
        #     root = stack.pop()
        #     if root.val == preVal:
        #         curr_count+=1
        #     else:
        #         curr_count = 1
        #     if curr_count == ans:
        #         res.append(root.val)
        #     if curr_count > ans:
        #         res=[]
        #         res.append(root.val)
        #         ans = curr_count
        #     preVal = root.val
        #     root = root.right
