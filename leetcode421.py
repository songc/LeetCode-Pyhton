# 421. 数组中两个数的最大异或值
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
from typing import List

class Trie:
    def __init__(self, val):
        self.val = val
        self.child = {}

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums)))-2
        root = Trie(-1)
        def add(num):
            tree = root
            for i in range(L,-1,-1):
                tmp = (num>>i)&1
                if tmp not in tree.child:
                    tree.child[tmp]=Trie(tmp)
                tree = tree.child[tmp]
        for n in nums:
            add(n)
        ans = 0
        for n in nums:
            t = 0
            tree = root
            for i in range(L,-1,-1):
                tmp = (n>>i)&1
                if 1-tmp in tree.child:
                    t = t*2+1
                    tree=tree.child[1-tmp]
                else:
                    t = t*2
                    tree = tree.child[tmp]
            ans = max(ans,t)
        return ans

sol = Solution()
nums = [2,8,10]
print(sol.findMaximumXOR(nums))