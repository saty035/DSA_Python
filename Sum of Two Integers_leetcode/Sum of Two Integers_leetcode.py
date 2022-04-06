# solved by satyam kumar
# question link https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:

        if ((a>=0 and b>=0 ) or (a<0 and b<0)):
            a=abs(a)
            for i in range(abs(b)):
                a+=1
            if (a>=0 and b>=0 ):
                return a
            else:
                return -a
        
        if (a>=0 and b<0):
            a=abs(a)
            for i in range(b,0):
                a-=1
            return a
                
        if (a<0 and b>=0):
            b=abs(b)
            for i in range(a,0):
                b-=1
            return b
                
            
                