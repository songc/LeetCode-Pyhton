# 667. 优美的排列 II
# 给你两个整数 n 和 k ，请你构造一个答案列表 answer ，该列表应当包含从 1 到 n 的 n 个不同正整数，并同时满足下述条件：

# 假设该列表是 answer = [a1, a2, a3, ... , an] ，那么列表 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数。
# 返回列表 answer 。如果存在多种答案，只需返回其中 任意一种 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/beautiful-arrangement-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List

# 从小到大排列不可以
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        vset = set(range(2,n+1))
        ans = []
        while k>0:
            if ans[-1]+k in vset:
                vset.remove(ans[-1]+k)
                ans.append(ans[-1]+k)
            else:
                vset.remove(ans[-1]-k)
                ans.append(ans[-1]-k)
            k-=1
        if vset:
            ans.extend(sorted(vset))
        return ans

# 从大到小排列可以
class Solution2:
    def constructArray(self, n: int, k: int) -> List[int]:
        vset = set(range(1,n))
        ans = [n]
        while k>0:
            if ans[-1]+k in vset:
                vset.remove(ans[-1]+k)
                ans.append(ans[-1]+k)
            else:
                vset.remove(ans[-1]-k)
                ans.append(ans[-1]-k)
            k-=1
        ans.reverse()
        if vset:
            return sorted(vset)+ans
        return ans



sol = Solution2()
n = 5
k = 2
print(sol.constructArray(n,k))        
