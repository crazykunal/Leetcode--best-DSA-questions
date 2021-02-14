class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # (O(n3) solution
        
#         k=""
#         for i in range(len(s)):
#           for j in range(i,len(s)):
#               if(s[i:j+1]==s[i:j+1][::-1]):
#                     if(len(k)<len(s[i:j+1])):
#                        k=s[i:j+1]         
#         return k
        
        n=len(s)
        dp=[[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i]=1
        m=1
        start=0
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
                start=i
                m=2
        for k in range(3,n+1):
            for i in range(0,n-k+1):
                j=i+k-1
                if s[i]==s[j] and dp[i+1][j-1]==1:
                    dp[i][j]=1
                    if m<k:
                        m=k
                        start=i  
        return s[start:start+m]
            


        # O(n2) solution
        
        # def ExpandAroundCenter(s,i,j):
        #     while(i>=0 and j<len(s) and s[i]==s[j]):
        #         i-=1
        #         j+=1
        #     return j-i-1 
        # if(s is None or len(s)<1):
        #     return ""
        # start=end=0
        # for i in range(0,len(s)):
        #     len1=ExpandAroundCenter(s,i,i)
        #     len2=ExpandAroundCenter(s,i,i+1)
        #     len3=max(len1,len2)
        #     if(len3>end-start):
        #         start=i-(len3-1)//2
        #         end=i+len3//2
        # return s[start:end+1]           
            
            
        # O(n) solution
        
        # T = '$#'+'#'.join(s)+'#%'
        # n = len(T)
        # P = [0] * n
        # C = R = 0
        # for i in range (1, n-1):
        #     if(R>i): 
        #       P[i] = min(R - i, P[2*C - i])
        #     while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
        #         P[i] += 1
        #     if i + P[i] > R:
        #         C = i
        #         R = i + P[i]
        # maxLen=centerIndex=0
        # for i in range(1,n-1):
        #     if(P[i]>maxLen):
        #         maxLen=P[i]
        #         centerIndex=i
        # return s[(centerIndex-maxLen)//2: (centerIndex  + maxLen)//2]
