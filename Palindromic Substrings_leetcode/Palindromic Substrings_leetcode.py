# solved by satyam kumar
# question link https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
       
        num=0
      
        
        for i in range(len(s)):
            # odd length palindrome
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                num+=1
               
                r+=1
                l-=1
            
            # even length palindrome
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                num+=1
                
                r+=1
                l-=1
        return num