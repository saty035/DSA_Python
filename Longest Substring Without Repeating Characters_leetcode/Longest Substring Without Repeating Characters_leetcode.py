# solved by satyam kumar
# question link https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst=[]
        num=0
        k=0
        i=0
        
        # using a pointer from begining and storing substring in list
        # and move pointer after repeatation
        
        while i<len(s):
            if s[i] not in lst:
                lst.append(s[i])
                num=max(num,len(lst))
                i+=1
            else:
                lst=[]
                k+=1
                i=k
        return num
            
            
            
        