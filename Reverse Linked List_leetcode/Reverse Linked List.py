# solved by satyam kumar
# question link https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
    # using two pointer
        prev,curr=None,head
        
        while curr!=None:
            
            # using temp to store address
            temp=curr.next
            
            # reversing the direction
            curr.next=prev
            prev=curr
            curr=temp
        return prev
        