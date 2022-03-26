# Solved by Satyam Kumar
# question link : https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums) :
    
        
        x=len(set(nums))
        y=len(nums)
        print(x,y)
        if  x==y :
            return False
        else:
            return True