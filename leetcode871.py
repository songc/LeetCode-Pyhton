# 871. 最低加油次数
# 汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。

# 沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。

# 假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。

# 当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

# 为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。

# 注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/minimum-number-of-refueling-stops
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans = 0
        curr = startFuel
        h = []
        ind = 0
        while curr<target:
            while ind<len(stations) and stations[ind][0]<=curr:
                heapq.heappush(h,-stations[ind][1])
                ind+=1
            if h:
                curr-=heapq.heappop(h)
                ans+=1
            else:
                break
        if curr>=target:
            return ans
        else:
            return -1

sol = Solution()
# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]

target = 100
startFuel = 50
stations = [[25,25],[50,50]]
print(sol.minRefuelStops(target,startFuel,stations))

