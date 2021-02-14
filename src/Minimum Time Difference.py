class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        import sys
        mark=[0]*(24*60)
        for time in timePoints:
            t=time.split(":")
            h=int(t[0])
            m=int(t[1])
            if(mark[h*60+m]):
                return 0
            mark[h*60+m]=True
        prev=0
        min1=sys.maxsize
        first=sys.maxsize
        last=-sys.maxsize
        for i in range(24*60):
            if(mark[i]):
                if(first!=sys.maxsize):
                    min1=min(min1,i-prev)
                first=min(first,i)
                last=max(last,i)
                prev=i
        min1=min(min1,(24*60-last+first))
        return min1
            
