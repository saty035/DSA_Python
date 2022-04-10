# solved by satyam kumar (reference https://www.youtube.com/watch?v=H9bfqozjoqs)
# question link https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # list to keep track of no of coin used for i'th amount
        # keeping the values max to get the min coins neccessary
        dp=[amount+1]*(amount+1)
        
        # 0 coin will be used for 0 amount
        dp[0]=0
        
        for a in range(1,amount+1):
            for c in coins:
            
                # if case is valid
                if a-c>=0:
                    # we will store the no. of coin used at a'th index
                    # 1 is added to keep count of itself too
                    dp[a]=min(dp[a],1+dp[a-c])
         
        return dp[amount] if dp[amount]!=amount+1 else -1
            
                
        