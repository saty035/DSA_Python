# solved by satyam kumar (reference https://www.youtube.com/watch?v=Y0lT9Fck7qI )
# question link https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # using dynamic programming
        # after analysing the decision tree
        # the bottom up approach was most optimal
        # and it creates a fibonacci series pattern 
        # which is implemented below
        one=1
        two=1
        
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
            
        return one
            