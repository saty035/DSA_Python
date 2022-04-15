# solved by satyam kumar
# question link https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
    
            
        return str(x)==str(x)[::-1]
    
#         n=x
        
#         if x<0:
#             return False
#         for i in str(x):
#             # print(i,n%10)
#             if int(i)==n%10:
#                 pass
#             else:
#                 return False
#             n=n//10
            
#         return True
        
            
        
        
            
        