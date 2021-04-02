# 765. 情侣牵手
# N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位。

# 人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。

# 这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/couples-holding-hands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        parent =[i for i in range(n//2)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(y)]=find(x)

        for i in range(0,n,2):
            union(row[i]//2,row[i+1]//2)
        v = set()   
        for i in range(n//2):
            v.add(find(i))
        return n//2-len(v)

sol = Solution()
row = [0, 1, 2, 3]

print(sol.minSwapsCouples(row))
