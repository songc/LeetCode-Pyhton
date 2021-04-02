# 75. 颜色分类
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-colors
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pre = 0
        for i in range(len(nums)):
            if nums[i]==0:
                if i==pre:
                    pre+=1
                else:
                    nums[pre],nums[i]=nums[i],nums[pre]
                    pre+=1
        for i in range(pre,len(nums)):
            if nums[i]==1:
                if i==pre:
                    pre+=1
                else:
                    nums[pre],nums[i]=nums[i],nums[pre]
                    pre+=1

sol = Solution()
nums=[2,0,2,1,1,0]
print(sol.sortColors(nums))
print(nums) 