# solved by satyam kumar (reference https://www.youtube.com/watch?v=WTzjTskDFMg)
# question link https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        dict={')':'(','}':'{',']':'['}
        st=[]
        
        for c in  s:
           
            if c in dict:
                
                # for closing parentheses
                if st and st[-1]==dict[c]:
                    # pop if pair seen
                    st.pop()
                    
                else:
                    # irrelevent sequence
                    return False
                
            else:
                # for open parentheses
                st.append(c)
      
        
        if not st:
            return True
        else:
            return False
                
        
   
                
                
    
               

        