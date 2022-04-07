# solved by satyam kumar (reference https://www.youtube.com/watch?v=XIdigk956u0)
# question link https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # empty list
        tail=ListNode()
        dummy=tail
        
        
        while list1 and list2:
            
            # comparing and assigning
            if list1.val < list2.val:
                dummy.next=list1
                list1=list1.next
            else:
                dummy.next=list2
                list2=list2.next
        
            dummy=dummy.next
        
        # if length of list aren't equal
        if list1:
            dummy.next=list1
        elif list2:
            dummy.next=list2
        
        return tail.next
                




