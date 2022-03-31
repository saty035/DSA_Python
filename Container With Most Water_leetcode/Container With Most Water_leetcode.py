# solved by satyam kumar
# question link https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force
#         max_area=0
#         area=0
#         for i in range(len(height)):
#             for j in range(i+1,len(height)):
#                 # print(i,height[i],"  ",j,height[j])
                
#                 if(height[i]<height[j]):
#                     area=(j-i)*height[i]
#                 else:
#                     area=(j-i)*height[j]
#                 # print(area,'\n')
                
#                 if area>max_area:
#                     max_area=area
      
#         return max_area

   
        area=0
        i=0
        j=len(height)-1
         # using two pointer from each end and comparing areas
        while(i<j):
            
            area=max(area,(j-i)*min(height[i],height[j]))
            
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area