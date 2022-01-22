# 1345. 跳跃游戏 IV
# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。

# 每一步，你可以从下标 i 跳到下标：

# i + 1 满足：i + 1 < arr.length
# i - 1 满足：i - 1 >= 0
# j 满足：arr[i] == arr[j] 且 i != j
# 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。

# 注意：任何时候你都不能跳到数组外面。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game-iv
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from cmath import inf
from typing import List
import collections

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n<=2:
            return n-1
        vdict = collections.defaultdict(list)
        for i in range(n):
            vdict[arr[i]].append(i)
        dist=[inf for _  in range(n)]
        deque = collections.deque([0])
        dist[0] = 0
        while deque:
            ind = deque.popleft()
            if ind==n-1:
                return dist[n-1]
            if arr[ind] in vdict:
                for i in vdict[arr[ind]]:
                    if dist[i]==inf:
                        deque.append(i)
                        dist[i]=dist[ind]+1
                vdict.pop(arr[ind])
            if ind-1>0 and dist[ind-1]==inf:
                dist[ind-1]=dist[ind]+1
                deque.append(ind-1)
            if ind+1<n and dist[ind+1]==inf:
                dist[ind+1]=dist[ind]+1
                deque.append(ind+1)
        return n-1
            
            


sol = Solution()
arr = [51,64,-15,58,98,31,48,72,78,-63,92,-5,64,-64,51,-48,64,48,-76,-86,-5,-64,-86,-47,92,-41,58,72,31,78,-15,-76,72,-5,-97,98,78,-97,-41,-47,-86,-97,78,-97,58,-41,72,-41,72,-25,-76,51,-86,-65,78,-63,72,-15,48,-15,-63,-65,31,-41,95,51,-47,51,-41,-76,58,-81,-41,88,58,-81,88,88,-47,-48,72,-25,-86,-41,-86,-64,-15,-63]
print(sol.minJumps(arr))