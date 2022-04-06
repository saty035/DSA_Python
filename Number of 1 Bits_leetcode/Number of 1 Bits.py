# solved by satyam kumar
# question link https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        x=0
        for i in bin(n).replace('0b',''):
            x=x+int(i)
        return x
            
        