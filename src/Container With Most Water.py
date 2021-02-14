class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # maxarea=0
        # for i in range(0,len(height)):
        #     for j in range(i+1,len(height)):
        #         maxarea=max(maxarea,min(height[i],height[j])*(j-i))
        # return maxarea
        
        
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return water
    
            
                
               
            
