# 剑指 Offer II 115. 重建序列
# 给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。
# 检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 sequences ，可能存在多个有效的 超序列 。

# 例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。
# 而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。
# 如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。
# 子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/ur2n8P
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        vnum1 = collections.defaultdict(set)
        vnum2 = collections.defaultdict(set)
        for seque in sequences:
            if len(seque)<=1:
                continue
            for i in range(1,len(seque)):
                vnum2[seque[i]].add(seque[i-1])
                vnum1[seque[i-1]].add(seque[i])
        tmp = []
        for i in range(1,len(nums)+1):
            if i not in vnum2:
                tmp.append(i)
        ans = []
        while len(tmp)==1:
            ans.append(tmp[0])
            tmp2 = []
            for i in vnum1[tmp[0]]:
                vnum2[i].remove(tmp[0])
                if len(vnum2[i])==0:
                    tmp2.append(i)
            tmp=tmp2
        return ans == nums

sol = Solution()
nums = [1,2,3]
sequences = [[1,2],[1,3],[2,3]]
print(sol.sequenceReconstruction(nums, sequences))
            
