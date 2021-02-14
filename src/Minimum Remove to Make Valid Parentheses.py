class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, ret = [], ['']*len(s)        
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            elif c==')':
                if stack:
                    left=stack.pop()
                    ret[left] = s[left]
                    ret[i] = c
            else:
                ret[i] = c
        return ''.join(ret)       
