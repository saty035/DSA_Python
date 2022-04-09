# solved by satyam kumar 
# question link https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # for string index of all zeros
        zero=[]
        
        # finding zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zero.append([i,j])
                    
    
        # replacing rows with zeros
        for x in zero:
            for i in range(len(matrix)):
                matrix[i][x[1]]=0
                
        # replacing columns with zero
        for x in zero:
            for i in range(len(matrix[0])):
                matrix[x[0]][i]=0
                    