import heapq
class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if k==1:
            return nums
        h=[]
        res=[]
        for i,n in enumerate(nums):
            self.addList(h,n)  
            if i>=k-1:
                res.append(h[0])
                self.popList(h,nums[i-k+1])
        return res
    def addList(self, hlist:list, item: int):
        while (hlist):
            if hlist[-1]<item:
                hlist.pop()
            else:
                break
        hlist.append(item)

    def popList(self, hlist:list, item:int):
        if hlist[0]==item:
            hlist.pop(0)
