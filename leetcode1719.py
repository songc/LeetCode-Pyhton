# 1719. 重构一棵树的方案数
# 给你一个数组 pairs ，其中 pairs[i] = [xi, yi] ，并且满足：

# pairs 中没有重复元素
# xi < yi
# 令 ways 为满足下面条件的有根树的方案数：

# 树所包含的所有节点值都在 pairs 中。
# 一个数对 [xi, yi] 出现在 pairs 中 当且仅当 xi 是 yi 的祖先或者 yi 是 xi 的祖先。
# 注意：构造出来的树不一定是二叉树。
# 两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。

# 请你返回：

# 如果 ways == 0 ，返回 0 。
# 如果 ways == 1 ，返回 1 。
# 如果 ways > 1 ，返回 2 。
# 一棵 有根树 指的是只有一个根节点的树，所有边都是从根往外的方向。

# 我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 祖先 。根节点没有祖先。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import collections
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = collections.defaultdict(set)
        for x,y in pairs:
            adj[x].add(y)
            adj[y].add(x)
        root = None
        for node, neig in adj.items():
            if len(neig)==len(adj)-1:
                root=node
        if not root:
            return 0
        ans = 1
        for node, neig in adj.items():
            if node==root:
                continue
            currDeg = len(neig)
            parent = -1
            parentDeg = len(adj)
            for ne in neig:
                if currDeg<=len(adj[ne])<parentDeg:
                    parent=ne
                    parentDeg = len(adj[ne])
            if parent==-1 or any(ne != parent and ne not in adj[parent] for ne in neig):
                return 0
            if currDeg==parentDeg:
                ans=2
        return ans


sol = Solution()
pairs = [[1,2],[2,3],[2,4],[1,5]]
print(sol.checkWays(pairs))
