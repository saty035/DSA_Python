# solved by satyam kumar
# question link

class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        
        try:
            return s==re.findall(p,s)[0]
        except:
            return False
            

        