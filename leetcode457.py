# 457. 环形数组是否存在循环
# 存在一个不含 0 的 环形 数组 nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数：

# 如果 nums[i] 是正数，向前 移动 nums[i] 步
# 如果 nums[i] 是负数，向后 移动 nums[i] 步
# 因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。

# 数组中的 循环 由长度为 k 的下标序列 seq ：

# 遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# 所有 nums[seq[j]] 应当不是 全正 就是 全负
# k > 1
# 如果 nums 中存在循环，返回 true ；否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/circular-array-loop
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = set()
        flags = [0]*n
        pre=None
        def dfs(ind,flag,pre):
            if flags[ind]>0:
                return flags[ind]
            if (flag<0 and nums[ind]>0) or (flag>0 and nums[ind] < 0):
                return 1
            if ind in visited:
                if pre == ind:
                    return 1
                else:
                    return 2
            visited.add(ind)
            nextInd = (ind+nums[ind])%n
            if nextInd<0:
                nextInd = n+nextInd
            flags[ind]=dfs(nextInd,flag,ind)
            visited.remove(ind)
            return flags[ind]
        for i in range(n):
            if nums[i]>0:
                flag = dfs(i,1,i)
            else:
                flag = dfs(i,-1,i)
            if flag==2:
                return True
        return False

sol = Solution()
nums = [-1,-2,-3,-4,-5]
print(sol.circularArrayLoop(nums))