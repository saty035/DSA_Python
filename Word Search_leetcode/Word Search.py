# solved by satyam kumar (refernce https://www.youtube.com/watch?v=pfiQ_PS1g8E)
# question link https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row,col=len(board),len(board[0])
        
        # to backtrack our word
        path=set()
        
        def dfs(r,c,i):
            
            # accepting condition 
            if i==len(word):
                return True
            
            # all the rejecting corner condition
            if (r<0 or c<0 or
                r>=row or c>=col or
                word[i]!=board[r][c] or
                (r,c) in path):
                
                return False
            
            path.add((r,c))
            
            # recursion for checking each adjacent index
            res=(dfs(r+1,c,i+1) or
                 dfs(r-1,c,i+1) or
                 dfs(r,c+1,i+1) or
                 dfs(r,c-1,i+1))
            # emptying the path for next index
            path.remove((r,c))
            return res
    
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False
    