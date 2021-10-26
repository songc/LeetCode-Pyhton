# 496. 下一个更大元素 I
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

# 请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-greater-element-i
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

# 类似递归的方法
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        vDict = dict()
        vDict[nums2[-1]]=-1
        for i in range(n-2,-1,-1):
            tmp = nums2[i+1]
            while tmp<nums2[i] and tmp != -1:
                tmp = vDict[tmp]
            vDict[nums2[i]]=tmp
        res = []
        for i in nums1:
            res.append(vDict[i])
        return res

# 单调栈和哈希。时间复杂度和上一个方法一样
class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        vDict = dict()
        stack = []
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if stack:
                vDict[nums2[i]]=stack[-1]
            else:
                vDict[nums2[i]]=-1
            stack.append(nums2[i])
        return [vDict[i] for i in nums1]

sol = Solution2()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(sol.nextGreaterElement(nums1,nums2))