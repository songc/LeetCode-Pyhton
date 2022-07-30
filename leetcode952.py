# 952. 按公因数计算最大组件大小
# 给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图：

# 有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记；
# 只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。
# 返回 图中最大连通组件的大小 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/largest-component-size-by-common-factor
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from math import gcd
from typing import List


# 超时
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent=[i for i in range(len(nums))]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot = find(x)
            yroot = find(y)
            if xroot!=yroot:
                parent[xroot]=yroot
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                xroot = find(i)
                yroot = find(j)
                if xroot==yroot:
                    continue
                if gcd(nums[i],nums[j])>1:
                    union(i,j)
        vdict = collections.defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            r = find(i)
            vdict[r]+=1
            ans = max(ans,vdict[r])
        return ans



class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent=[i for i in range(max(nums)+1)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot = find(x)
            yroot = find(y)
            if xroot!=yroot:
                parent[yroot]=xroot
        for num in nums:
            i=2
            while i*i<=num:
                if num%i==0:
                    union(num,i)
                    union(num,num//i)
                i+=1

        vdict = collections.defaultdict(int)
        ans = 0
        for i in nums:
            r = find(i)
            vdict[r]+=1
            ans = max(ans,vdict[r])
        return ans


sol = Solution()
nums = [4,6,15,35]
print(sol.largestComponentSize(nums))
