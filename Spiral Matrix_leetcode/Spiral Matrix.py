# solved by satyam kumar (refernce https://www.youtube.com/watch?v=BJnMZNwUk1M)
# question link https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        
        while left < right and bottom > top:
            print(left ,right ,bottom ,top)
            # from left to right
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            print(left ,right ,bottom ,top)
            
            # from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right-=1
            print(left ,right ,bottom ,top)
            
            # for row matrix and column matrix
            if not (left < right and bottom > top):
                break
            
            # for right to left
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            
            # for whats left in left col
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
        return res
            
            