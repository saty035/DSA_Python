# solved by satyam kumar
# question link https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:

        B=bin(n)[2:].rjust(32,'0')[::-1]
        print(B)
        return int(B,2)
        