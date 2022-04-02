# solved by satyam kumar
# question link https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst=[]
        
        # iterating in i<=j portion
        for i in range(0,numRows):
            
            temp=[]
            for j in range(0,i+1):
                
                # appending the ones
                if  j==0 or i==j:
                    temp.append(1)
                else:
                    # appending the addition from previous lists
                    temp.append(lst[i-1][j]+lst[i-1][j-1])
            lst.append(temp)
        
        return lst
        
                    
                

            
            
            
        