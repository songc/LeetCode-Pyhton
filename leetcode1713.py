# 1713. 得到子序列的最少操作次数
# 给你一个数组 target ，包含若干 互不相同 的整数，以及另一个整数数组 arr ，arr 可能 包含重复元素。

# 每一次操作中，你可以在 arr 的任意位置插入任一整数。比方说，如果 arr = [1,4,1,2] ，那么你可以在中间添加 3 得到 [1,4,3,1,2] 。你可以在数组最开始或最后面添加整数。

# 请你返回 最少 操作次数，使得 target 成为 arr 的一个子序列。

# 一个数组的 子序列 指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的子序列（加粗元素），但 [2,4,2] 不是子序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import bisect

# 超时
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        m = len(target)
        n = len(arr)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,m+1):
            dp[0][i]=i
        for i in range(1,n+1):
            for j in range(1,m+1):
                if target[j-1]==arr[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1]+1,dp[i][j-1]+1)
        return dp[-1][-1]

class Solution2:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        
        idxDict = dict((num,i) for i, num in enumerate(target))
        stack = []
        for num in arr:
            if num in idxDict:
                idx = idxDict[num]
                i = bisect.bisect_left(stack,idx)
                if i == len(stack):
                    stack.append(0)
                stack[i]=idx
        return len(target)-len(stack)

sol = Solution2()
target = [6,4,8,1,3,2]
arr = [4,7,6,2,3,8,6,1]
print(sol.minOperations(target,arr))
                
