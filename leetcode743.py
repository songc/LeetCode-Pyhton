# 743. 网络延迟时间
# 有 n 个网络节点，标记为 1 到 n。

# 给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

# 现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/network-delay-time
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import heapq
import bisect
import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        tDict = collections.defaultdict(list)
        vDict = [float('inf')]*n
        vDict[k-1]=0
        for time in times:
            tDict[time[0]].append((time[1],time[2]))
        deque = collections.deque()
        deque.append((0,k))
        while deque:
            _,x = deque.popleft()
            for y, t in tDict[x]:
                if vDict[x-1]+t < vDict[y-1]:
                    vDict[y-1]=vDict[x-1]+t
                    bisect.insort(deque,(vDict[y-1],y))
        res = max(vDict)
        return res if res != float('inf') else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
sol = Solution()
print(sol.networkDelayTime(times,n,k))

            
                
            
                