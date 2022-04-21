# solved by satyam kumar
# question link https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
                #last index
        n=len(nums2)
        m=len(nums1)
        for i in range(n):
            nums1.append(0)
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
        if len(nums1)%2!=0:
            return nums1[len(nums1)//2]
        else:
            return (nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1])/2
        
        
        