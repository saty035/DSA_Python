# solved by satyam kumar
# question link https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst=[]
        for i in range(len(nums)//2):
            lst.append(nums[i])
            lst.append(nums[n])
            n+=1
        return lst
        