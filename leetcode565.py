# 565. 数组嵌套
# 索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。

# 假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/array-nesting
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import collections
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        def find(x, vset, currMin):
            if nums[x] in vset:
                nums[x]=currMin
                return currMin
            else:
                vset.add(nums[x])
                currMin=min(nums[x],currMin)
                nums[x]=find(nums[x],vset,currMin)
            return nums[x]
        vdict=collections.defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            vset = set()
            curr = len(nums)
            root = find(i,vset,curr)
            vdict[root]+=1
            if vdict[root]>ans:
                ans=vdict[root]
        return ans

class Solution2:
    def arrayNesting(self, nums: List[int]) -> int:
        vset=set()
        ans = 1
        for i in range(len(nums)):
            curr=0
            tmp = i
            while tmp not in vset:
                vset.add(tmp)
                curr+=1
                tmp=nums[tmp]
            ans = max(curr,ans)
        return ans
                




sol = Solution2()
nums = [5,4,0,3,1,6,2]
print(sol.arrayNesting(nums))