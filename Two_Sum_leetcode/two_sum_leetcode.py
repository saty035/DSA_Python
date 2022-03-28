# solved by satyam kumar
# question link: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(j>i):
                    if(target-nums[i]==nums[j]):
                        return [i,j]
        