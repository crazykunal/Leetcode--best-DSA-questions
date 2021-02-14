class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length = len(nums)
        # L, R, answer = [0]*length, [0]*length, [0]*length
        # L[0] = 1
        # for i in range(1, length):
        #     L[i] = nums[i - 1] * L[i - 1]
        # R[length - 1] = 1
        # for i in reversed(range(length - 1)):
        #     R[i] = nums[i + 1] * R[i + 1]
        # for i in range(length):
        #     answer[i] = L[i] * R[i]
        # return answer
        
        
        if not nums: return False
        ans=[0]*len(nums)
        ans[0] = 1
        for i in range(1,len(nums)):
            ans[i]=nums[i-1]*ans[i-1]
        R=1
        for i in reversed(range(len(nums))):
            ans[i]=ans[i]*R
            R*=nums[i]
        return ans
