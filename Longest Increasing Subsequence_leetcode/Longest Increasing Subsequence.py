# solved by satyam kumar (refernce https://www.youtube.com/watch?v=cjWnW0hdF1Y)
# question link https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # creating cache
        lst=[1]*len(nums)
        
        # iterating from end
        for i in range(len(nums)-1,-1,-1):
            # iterating from ith index till end
            for j in range(i+1,len(nums)):
                
                # increasing condition
                if nums[i]<nums[j]:
                    # update the list
                    lst[i]=max(lst[i],1+lst[j])
        return max(lst)
      