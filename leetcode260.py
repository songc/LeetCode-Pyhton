# 260. 只出现一次的数字 III
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

#  

# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-number-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nset = set()
        for n in nums:
            if n in nset:
                nset.remove(n)
            else:
                nset.add(n)
        return list(nset)


class Solution2:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xornum = 0
        for n in nums:
            xornum ^=n
        lsp = xornum & (-xornum)
        x1=x2=0
        for n in nums:
            if lsp&n:
                x1^=n
            else:
                x2^=n
        return [x1,x2]



sol = Solution2()
nums = [1,2,1,3,2,5]
print(sol.singleNumber(nums))