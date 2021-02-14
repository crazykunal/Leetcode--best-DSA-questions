class Solution:
    def minSubArrayLen(self, s: int, A: List[int]) -> int:
        # import sys
        # n=len(A)
        # ans=sys.maxsize
        # flag=0
        # for i in range(n):
        #     sum = 0
        #     for j in range(i,n):
        #         sum+=A[j]
        #         if(sum>=s):
        #             ans = min(ans, j-i+1)
        #             flag=1
        #             break
        # if(flag):
        #     return ans
        # else:
        #     return 0
        
        import sys
        n=len(A)
        ans=sys.maxsize
        l,sum1=0,0
        for i in range(0,n):
            sum1+=A[i]
            while(sum1>=s):
                ans=min(ans,i-l+1)
                sum1-=A[l]
                l+=1
        if(ans!=sys.maxsize):
            return ans
        else:
            return 0
