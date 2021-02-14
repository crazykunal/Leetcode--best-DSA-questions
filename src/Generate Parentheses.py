class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # ans = []
        # def backtrack(S = '', left = 0, right = 0):
        #     if len(S) == 2 * n:
        #         ans.append(S)
        #         return
        #     if left < n:
        #         backtrack(S+'(', left+1, right)
        #     if right < left:
        #         backtrack(S+')', left, right+1)
        # backtrack()
        # return ans
        
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l-r<0 or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        return res  
                                    
