# solved by satyam kumar
# question link https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if root is empty or value
        if root==None or root.val==val:
            return root
        
        # adjusting the root according the value
        if root.val>val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
     
            
        
        