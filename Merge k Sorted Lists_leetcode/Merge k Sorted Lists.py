# solved by satyam kumar (reference https://www.youtube.com/watch?v=q5a5OiGbT6Q)
# question link https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # approach 1
#         if len(lists)==0:
#             return ListNode().next
#         if len(lists)==1:
#             return lists[0]
        
        
#         tail=ListNode()
#         temp=lists[0]
        
#         for i in range(1,len(lists)):
            
#             dummy=tail
            


#             while temp and lists[i]:

#                 # comparing and assigning
#                 if temp.val < lists[i].val:
#                     dummy.next=temp
#                     temp=temp.next
#                 else:
#                     dummy.next=lists[i]
#                     lists[i]=lists[i].next
#                 dummy=dummy.next

#             # if length of list aren't equal
#             if temp:
#                 dummy.next=temp
#             elif lists[i]:
#                 dummy.next=lists[i]
#             temp=tail.next
#             # print(tail)
            
#         return tail.next

        # approach 2
        if not lists or len(lists)==0:
            return None
        
        # until our sublists are merged in one list
        while len(lists)>1:
            mergedLists=[]
            
            # merging pair and reducing length of lists
            for i in range(0,len(lists),2):
                l1=lists[i]
                if (i+1)<len(lists):
                    l2=lists[i+1]
                else:
                    l2=None
                mergedLists.append(self.mergelist(l1,l2))
            
            lists=mergedLists
        return lists[0]
            
            
    def mergelist(self,list1,list2):
        tail=ListNode()
        dummy=tail
        
        
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next=list1
                list1=list1.next
            else:
                dummy.next=list2
                list2=list2.next
            
            dummy=dummy.next
        
        if list1:
            dummy.next=list1
        elif list2:
            dummy.next=list2
        
        return tail.next
                