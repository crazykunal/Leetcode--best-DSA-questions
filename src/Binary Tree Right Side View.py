# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # result = []
        # if not root:
        #     return result
        # q = deque()
        # q.append(root)
        # while q:
        #     level_len = len(q)
        #     for _ in range(level_len):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     result.append(node.val)
        # return result
        
        def dfs(root, level, res):
            if root:
                if len(res) == level:
                    res.append(root.val)
                dfs(root.right, level+1, res)
                dfs(root.left, level+1, res)
        res = []
        dfs(root, 0, res)
        return res

        
