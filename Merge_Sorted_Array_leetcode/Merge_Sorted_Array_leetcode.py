# implementation reference https://www.youtube.com/watch?v=P1Ic85RarKY
# question link https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #last index
        lst=n+m-1
        
        
        # merging from last index
        while m>0 and n>0:
            
            if nums1[m-1] > nums2[n-1]:
                nums1[lst]=nums1[m-1]
                m-=1
            else:
                nums1[lst]=nums2[n-1]
                n-=1
            lst-=1
        
        # for remaining values in nums2
        while n>0:
            nums1[lst]=nums2[n-1]
            n-=1
            lst-=1
        
        