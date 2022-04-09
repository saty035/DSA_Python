# solved by satyam kumar
# question link https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left,right=0,len(matrix)-1
        top,bottom=0,len(matrix)-1
        
        for i in range(len(matrix)//2):
            while ( left != right) :
            
                temp=matrix[top][left]

                matrix[top][left]=matrix[bottom][top]

                matrix[bottom][top]=matrix[right][bottom]

                matrix[right][bottom]=matrix[left][right]

                matrix[left][right]=temp

                left+=1
                bottom-=1
            top+=1
            left=top
            right-=1
            bottom=right

            
        