# solved by satyam kumar (reference https://www.youtube.com/watch?v=edfGASf_QxE)
# question link https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base condition
        if not p and not q:
            return True
        # corner condition
        if (not p or not q) or p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
                
    
        
        
            

        