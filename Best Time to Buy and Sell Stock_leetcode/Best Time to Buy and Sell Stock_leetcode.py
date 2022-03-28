class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         profit=0
#         for i in range(0,len(prices)-1):
#             for j in range(i+1,len(prices)):
#                 if(prices[j]>prices[i] and prices[j]-prices[i]>profit):
                   
#                     profit=prices[j]-prices[i]
#         return profit
        
    
#         a=prices.index(min(prices))  
#         b=prices.index(max(prices[a+1:]))
#         if prices[b]-prices[a]>0:
#                        return prices[b]-prices[a]
#         else:
#                        return 0
                       
        profit=0
        l=0
        r=1
        
        while(r<len(prices)):
            print(prices[l],prices[r])
            if(prices[r]>prices[l] ):
                if prices[r]-prices[l]>profit:
                    profit=prices[r]-prices[l]
                r+=1
                
            else:
                l=r
                r+=1
        return profit
        
        