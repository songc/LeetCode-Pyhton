# 179. 最大数
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
from typing import List
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def func(n1,n2):
            s1 = n1+n2
            s2 = n2+n1
            if s1>s2:
                return 1
            if s1==s2:
                return 0
            if s1<s2:
                return -1
        ans =  "".join(sorted((str(i) for i in nums),reverse=True, key=functools.cmp_to_key(func)))
        if ans.startswith("0"):
            return "0"
        return ans

sol = Solution()
nums = [3,30,34,5,9]
print(sol.largestNumber(nums))