# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res=0
#         for i in range(len(height)):
#             for k in range(1,len(height)):
#                 j=i+k
#                 if j>=len(height):
#                     break
#                 res = max(res,min(height[i],height[j])*k)
#         return res

class Solution:
    def maxArea(self, height: list) -> int:
        lo=0
        hi=len(height)-1
        res = 0
        while(lo<hi):
            res = max(res,min(height[lo],height[hi])*(hi-lo))
            if height[lo]<=height[hi]:
                t = height[lo]
                while(height[lo]<=t and lo<hi):
                    lo+=1
            else:
                t = height[hi]
                while(height[hi]<=t and lo<hi):
                    hi-=1
        return res
