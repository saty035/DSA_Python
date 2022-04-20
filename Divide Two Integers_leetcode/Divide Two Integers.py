# solved by satyam kumar
# question link https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if math.trunc(dividend/divisor)>pow(2,31)-1:
            return pow(2,31)-1
        elif math.trunc(dividend/divisor)<-pow(2,31):
            return -pow(2,31)
        else:    
            return dividend//divisor if (dividend>=0 and divisor>0) else math.trunc(dividend/divisor)
        