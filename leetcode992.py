# 992. K 个不同整数的子数组
# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。

# （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）

# 返回 A 中好子数组的数目。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subarrays-with-k-different-integers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ans = 0 
        n = len(A)
        for i in range(n):
            if i+K>n:
                break
            # tmpDict = collections.defaultdict(int)
            keySet = set()
            for j in range(i,i+K):
                # tmpDict[A[i]]+=1
                keySet.add(A[j])
            if len(keySet)==K:
                ans+=1
            j = j+1
            while j<n:
                # tmpDict[A[j]]+=1
                keySet.add(A[j])
                if len(keySet)==K:
                    ans+=1
                elif len(keySet)>K:
                    break
                j+=1
        return ans

sol = Solution()
A=[2,2,1,2,2,2,1,1]
K=2
print(sol.subarraysWithKDistinct(A,K))
        