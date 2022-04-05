# solved by satyam kumar (refernce https://www.youtube.com/watch?v=XYQecbcd6_c)
# question link : https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        rev=''
        revlen=0
        
        for i in range(len(s)):
            # odd length palindrome
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>revlen:
                    rev=s[l:r+1]
                    revlen=r-l+1
                r+=1
                l-=1
            
            # even length palindrome
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>revlen:
                    rev=s[l:r+1]
                    revlen=r-l+1
                r+=1
                l-=1
        return rev
            
        

            
                
                
       
    
        
       