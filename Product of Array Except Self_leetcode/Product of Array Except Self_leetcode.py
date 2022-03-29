# solved by Satyam Kumar , reference https://www.youtube.com/watch?v=bNvIQI2wAjk
# question link https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # create prefix sum 
        prefix=[1]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]*nums[i-1])
        
        #create postfix sum (reverse)
        postfix=[1]
        for i in range(len(nums)-2,-1,-1):
            
            postfix.append(postfix[len(nums)-2-i]*nums[i+1])
        print(postfix)
        
        # product of prefix and postfix
        output=[]
        for i in range(len(nums)):
            output.append(prefix[i]*postfix[len(nums)-1-i])
        
        return output
            
            
        
        