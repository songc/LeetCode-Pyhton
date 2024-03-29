# 1640. 能否连接形成数组
# 给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，其中的整数也 互不相同 。请你以 任意顺序 连接 pieces 中的数组以形成 arr 。但是，不允许 对每个数组 pieces[i] 中的整数重新排序。

# 如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/check-array-formation-through-concatenation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        vdict = dict()
        for p in pieces:
            vdict[p[0]]=p
        tmp = []
        while len(tmp)<len(arr):
            n = len(tmp)
            if arr[n] in vdict:
                tmp.extend(vdict[arr[n]])
            else:
                return False
            for i in range(n,n+len(vdict[arr[n]])):
                if tmp[i]!=arr[i]:
                    return False
        return True

arr = [15,88]
pieces = [[88],[15]]
sol = Solution()
print(sol.canFormArray(arr,pieces))