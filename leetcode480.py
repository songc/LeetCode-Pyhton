# 480. 滑动窗口中位数
# 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
import bisect
import collections
class Solution:
    def medianSlidingWindow(self, nums: list, k: int) -> list:
        ans =[]
        tmpNum=[]
        for ind, i in enumerate(nums):
            if len(tmpNum)<k:
                bisect.insort_right(tmpNum,i)
                if len(tmpNum)==k:
                    tmp = (tmpNum[k//2]+tmpNum[(k-1)//2])/2
                    ans.append(tmp)
                continue
            tmpNum.pop(bisect.bisect_left(tmpNum,nums[ind-k]))
            bisect.insort_right(tmpNum,i)
            tmp = (tmpNum[k//2]+tmpNum[(k-1)//2])/2
            ans.append(tmp)
        return ans

sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.medianSlidingWindow(nums,k))
            
