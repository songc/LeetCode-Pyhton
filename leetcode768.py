# 768. 最多能完成排序的块 II
# 这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。

# arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

# 我们最多能将数组分成多少块？

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/max-chunks-to-make-sorted-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        tmp = sorted(arr)
        vdict1 = collections.defaultdict(int)
        vdict2 = collections.defaultdict(int)
        for i,j in zip(arr,tmp):
            vdict1[i]+=1
            vdict2[j]+=1
            if vdict1==vdict2:
                ans+=1
        return ans

sol = Solution()
arr = [2,1,3,4,4]
print(sol.maxChunksToSorted(arr))
            

        