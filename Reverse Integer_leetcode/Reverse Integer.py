# solved by satyam kumar
# question link https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        
        # reversing the integer by converting into string and checking the condition for 32-bit while returning 
        if x<0:
            return -int(str(abs(x))[::-1]) if -pow(2,31)<-int(str(abs(x))[::-1])<=pow(2,31) else 0
        else:
            return int(str(x)[::-1]) if -pow(2,31)<int(str(x)[::-1])<=pow(2,31) else 0
        
