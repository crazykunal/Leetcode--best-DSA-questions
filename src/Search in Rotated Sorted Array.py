class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while(l<h):
            mid=l+(h-l)//2
            if(nums[mid]>nums[h]):
                l=mid+1
            else:
                h=mid
        start=l
        l=0
        h=len(nums)-1
        if(nums[start]<=target<=nums[h]):
            l=start
        else:
            h=start
        while(l<=h):
            mid=l+(h-l)//2
            if(nums[mid]==target):
                return mid
            if(nums[mid]<target):
                l=mid+1
            else:
                h=mid-1
        return -1
            
          
        
#         if not nums:
#             return -1

#         low, high = 0, len(nums) - 1

#         while low <= high:
#             mid = (low + high) // 2
#             if target == nums[mid]:
#                 return mid

#             if nums[low] <= nums[mid]:
#                 if nums[low] <= target <= nums[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             else:
#                 if nums[mid] <= target <= nums[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1

#         return -1
