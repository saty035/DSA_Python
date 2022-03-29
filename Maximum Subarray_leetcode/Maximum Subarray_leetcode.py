# Solved by Satyam Kumar , reference video https://www.youtube.com/watch?v=5WZl3MMT0Eg
# Question link https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane algo
        
        sum=0
        max_=nums[0]
        
        # carry the subarray sum until it gives negative sum
        # when it gives a negative sum reset it to 0 

        
        for i in range(len(nums)):
            if sum<0:
                sum=0
            
            sum=sum+nums[i]
            if max_<sum:
                max_=sum
            
            
        return max_
                