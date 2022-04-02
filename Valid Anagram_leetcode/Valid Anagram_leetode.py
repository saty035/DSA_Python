# solved by satyam kumar
# question link https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        
        # for i in t:
        #     if i in s:
        #         #print(s)
        #         s=s.replace(i,'',1)
        #     else:
        #         return False
        
                
        d1=dict(Counter(s))
        d2=dict(Counter(t))
        for i in d1:
            if d1[i]!=d2.get(i):
                return False

        return True

        