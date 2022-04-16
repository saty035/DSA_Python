# solved by satyam kumar
# question link https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # assigning carry with 0
        carry=0
        
        # return list
        l3=ListNode()
        pt=l3
       
        while True:
            
            # after traversal of both the lists
            if l1==None and l2==None:
                
                # corner case for last node in l3
                if carry>0:    
                    l3.next=ListNode(carry)
                    return pt.next
                else:
                    return pt.next
                
            # l2 is longer
            if l1==None:
                l3.next=ListNode((l2.val + carry)%10)
                carry=(l2.val + carry)//10
                l2=l2.next
                
            # if l1 is longer
            elif l2==None:
                l3.next=ListNode((l1.val+ carry)%10 )
                carry=(l1.val + carry)//10
                l1=l1.next
                
            # both of same length
            else:
                l3.next=ListNode((l1.val + l2.val+ carry)%10 )
                carry= (l1.val + l2.val+carry)//10
                l1=l1.next
                l2=l2.next
            
            l3=l3.next
            
            
       