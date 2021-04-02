# 1319. 连通网络的操作次数
# 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

# 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

# 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def makeConnected(self, n: int, connections: list) -> int:
        connNums = len(connections)
        if connNums<n-1:
            return -1
        parent=[i for i in range(n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(y)]=find(x)
        for x, y in connections:
            union(x,y)
        vset=set()
        for i in range(n):
            vset.add(find(i))
        return len(vset)-1