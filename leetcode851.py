# 851. 喧闹和富有
# 有一组 n 个人作为实验对象，从 0 到 n - 1 编号，其中每个人都有不同数目的钱，以及不同程度的安静值（quietness）。为了方便起见，我们将编号为 x 的人简称为 "person x "。

# 给你一个数组 richer ，其中 richer[i] = [ai, bi] 表示 person ai 比 person bi 更有钱。另给你一个整数数组 quiet ，其中 quiet[i] 是 person i 的安静值。richer 中所给出的数据 逻辑自恰（也就是说，在 person x 比 person y 更有钱的同时，不会出现 person y 比 person x 更有钱的情况 ）。

# 现在，返回一个整数数组 answer 作为答案，其中 answer[x] = y 的前提是，在所有拥有的钱肯定不少于 person x 的人中，person y 是最安静的人（也就是安静值 quiet[y] 最小的人）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/loud-and-rich
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections
from functools import lru_cache

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dictTmp = collections.defaultdict(list)
        for ai,bi in richer:
            dictTmp[bi].append(ai)
        @lru_cache(None)
        def dfs(k):
            if k not in dictTmp:
                return k
            tmp = k
            for n in dictTmp[k]:
                newK = dfs(n)
                if quiet[tmp]>quiet[newK]:
                    tmp=newK
            return tmp
        res = []
        for i in range(len(quiet)):
            res.append(dfs(i))
        return res


        

sol = Solution()
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(sol.loudAndRich(richer,quiet))
        