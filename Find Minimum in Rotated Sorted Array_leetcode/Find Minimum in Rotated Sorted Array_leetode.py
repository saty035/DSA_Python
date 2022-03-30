# solved by satyam kumar
# question link https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        i=0
        j=len(nums)-1
        # use two pointer from both end
        
        if nums[0]<nums[len(nums)-1]:
                return nums[0]
        
        while len(nums)>=2:
            
            if nums[i]<nums[i+1]:
                i+=1
            else:
                return nums[i+1]
            
            
            if nums[j]>nums[j-1]:
                j-=1
            else:
                return nums[j]
            
        return nums[0]
        