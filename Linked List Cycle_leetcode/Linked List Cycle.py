# solved by satyam kumar (reference https://www.youtube.com/watch?v=gBTe7lFR3vc)
# question link https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#         x=[]
        
#         # for empty linked list
#         if head==None:
#             return False
        
#         while head.next!=None:
            
#             # if cycle exists
#             if head.next in x:
#                 return True
#             # storing the address
#             x.append(head.next)
#             head=head.next
            
#         return False
            
            
        slow=head
        fast=head
        
#         while True:
#             if slow==None or fast==None:
#                 return False
#             try:
#                 slow=slow.next
#                 fast=fast.next.next
#             except:
#                 return False
            
#             if slow==fast:
#                 return True

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        
        
            
        