
# 面试题 17.10. 主要元素
# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-majority-element-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return -1
        if n==1:
            return nums[0]
        res = nums[0]
        count = 1
        for i in range(1,n):
            if nums[i]==res:
                count+=1
            else:
                count-=1
                if count == 0:
                    res = nums[i]
                    count = 1
        count = 0
        for i in range(n):
            if nums[i]==res:
                count+=1
        if count >= (n+1)//2:
            return res
        else:
            return -1

sol = Solution()
nums = [1,2,5,9,5,9,5,5,5]
print(sol.majorityElement(nums))