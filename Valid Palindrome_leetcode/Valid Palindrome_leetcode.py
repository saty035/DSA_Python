# solved by satyam kumar
# question link https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha='qwertyuiopasdfghjklzxcvbnm1234567890'
        new=''
        # converting to lowercase
        s=s.lower()
        
        # fetching the ascii characters
        for i in range(len(s)):
            if s[i] in alpha:
                
                new=new+s[i]
        
        return new==new[::-1]

            
        