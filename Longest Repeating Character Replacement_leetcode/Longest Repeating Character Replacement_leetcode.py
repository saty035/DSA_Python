
# solved by satyam kumar (refernce https://www.youtube.com/watch?v=gqXU1UyA8pk)
# questin link https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using a hash map to keep count of alphabets
        count={}
        
        # left counter
        l=0
        res=0
        
        # iterating over right counter
        for r in range(len(s)):
            
            # assigning values
            count[s[r]]=1+ count.get(s[r],0)
            
            # checking replacement condition
            while (r-l+1)- max(count.values())>k:
                
                # reducing count
                count[s[l]]-=1
                
                # shifting left counter
                l+=1
            # storing max
            res=max((r-l+1),res)
            
            
        return res
        