class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # a=[[0]*n for i in range(n)]
        # rbegin,rend=0,n-1
        # cbegin,cend=0,n-1
        # c=1
        # while(rbegin<=rend and cbegin<=cend):
        #     for i in range(cbegin,cend+1):
        #         a[rbegin][i]=c
        #         c+=1
        #     rbegin+=1
        #     for i in range(rbegin,rend+1):
        #         a[i][cend]=c
        #         c+=1
        #     cend-=1
        #     if(rbegin<=rend):
        #         for i in range(cend,cbegin-1,-1):
        #             a[rend][i]=c
        #             c+=1
        #         rend-=1
        #     if(cbegin<=cend):
        #         for i in range(rend,rbegin-1,-1):
        #             a[i][cbegin]=c
        #             c+=1
        #         cbegin+=1
        # return a
        
        
        A = [[None] * n for _ in range(n)]
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        row,col,d=0,0,0
        for k in range(n*n):
            A[row][col] = k+1
            r=(row+dir[d][0])%n
            c=(col+dir[d][1])%n
            if(A[r][c]):
                d=(d+1)%4
            row+=dir[d][0]
            col+=dir[d][1]
        return A
    
