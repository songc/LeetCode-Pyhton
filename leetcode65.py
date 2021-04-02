# 665. 非递减数列
# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/non-decreasing-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def checkPossibility(self, nums: list) -> bool:
        count=i=0
        while i < len(nums)-1:
            if nums[i]<=nums[i+1]:
                i+=1
            else:
                count+=1
                if count>1:
                    return False
                if i==0:
                    i+=1
                elif i<len(nums)-2:
                    if nums[i]<=nums[i+2]:
                        i+=1
                    elif nums[i-1]>nums[i+1]:
                        return False
                    else:
                        i+=1
                else:
                    i+=1      
        return True







sol = Solution()
nums=[5,7,1,8]
print(sol.checkPossibility(nums))
