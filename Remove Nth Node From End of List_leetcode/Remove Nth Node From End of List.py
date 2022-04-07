# solved by satyam kumar
# question link https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
     
        # checking for single or empty list
        if head.next==None or head==None:
            return ListNode().next
        
        
        i=0
        len=1
        
        # poiinters
        l,r=head,head
        
        
        while r.next!=None:
            
            # shifting the right pointer by n from left pointer
            i+=1
            if i<=n:
                r=r.next
            else:
                l=l.next
                r=r.next
                
            len+=1
            
       # edge condition
        if l==head and n==len:
            head=head.next
        else:
            l.next=l.next.next
       
        
        return head
        