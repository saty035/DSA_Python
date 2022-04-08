# solved by satyam kumar (reference https://www.youtube.com/watch?v=S5bfdUTrKLM )
# question link https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
#         if head.next==None:
#             return head
        
#         while head!=None:
#             new=head
#             temp=head
#             i=0
#             try:
#                 while temp.next.next!=None:
#                     temp=temp.next
#                     i+=1
#             except:
#                 pass
            
#             if i>0:
#                 t=head.next
#                 head.next=temp.next
#                 temp.next.next=t
#                 temp.next=None
#                 head=head.next.next
#             else:
#                 head=head.next
            
            
#         return new

        # finding the middle
        slow,fast=head,head.next
        while fast and fast.next:
            
            slow=slow.next
            fast=fast.next.next
        
            
        second=slow.next
        prev=slow.next=None
       
        # reversing the second half of list
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
     
        # merging those two list
        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
  
            first,second=tmp1,tmp2
            
            
            
    
    
        
        
        