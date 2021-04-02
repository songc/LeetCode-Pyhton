# 31. 下一个排列
# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须 原地 修改，只允许使用额外常数空间。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<=1:
            return
        i = n-2
        while i>=0:
            if nums[i]<nums[i+1]:
                break
            i-=1
        if i>=0:
            for j in range(n-1,i,-1):
                if nums[j]>nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                    break
        left,right = i+1, n-1
        while left < right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        
sol = Solution()
nums=[3,2,1]
sol.nextPermutation(nums)
print(nums)
