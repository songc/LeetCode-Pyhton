# 456. 132模式
# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/132-pattern
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<=2:
            return False
        deque = []
        minNum = [nums[0]]
        for i in range(1,n):
            minNum.append(min(minNum[-1],nums[i]))
        for i in range(n-1,0,-1):
            if nums[i]>minNum[i]:
                while deque and deque[-1] <= minNum[i]:
                    deque.pop()
                if deque and deque[-1]<nums[i]:
                    return True
                deque.append(nums[i])
        return False

sol = Solution()
nums = [1,0,1,-4,-3]
print(sol.find132pattern(nums))
