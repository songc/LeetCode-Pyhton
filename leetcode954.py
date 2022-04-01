# 954. 二倍数对数组
# 给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/array-of-doubled-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
import collections


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        vdict = collections.defaultdict(int)
        for a in arr:
            if a/2 in vdict:
                vdict[a/2]-=1
                if vdict[a/2]==0:
                    del vdict[a/2]
            elif a*2 in vdict:
                vdict[a*2]-=1
                if vdict[a*2]==0:
                    del vdict[a*2]
            else:
                vdict[a]+=1
        return not vdict

sol = Solution()
arr = [4,-2,2,-4]
print(sol.canReorderDoubled(arr))