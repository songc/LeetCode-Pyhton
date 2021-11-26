# 752. 打开转盘锁
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/open-the-lock
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target=="0000":
            return 0
        deads = set(deadends)
        if "0000" in deads:
            return -1
        def num_prev(x: str) -> str:
            return "9" if x == "0" else str(int(x) - 1)
        
        def num_succ(x: str) -> str:
            return "0" if x == "9" else str(int(x) + 1)

        
        def get(status:str):
            s = list(status)
            for i in range(4):
                num = s[i]
                s[i]=num_prev(num)
                yield "".join(s)
                s[i]=num_succ(num)
                yield "".join(s)
                s[i]=num
        
        deque = collections.deque([("0000",0)])
        seen = {"0000"}
        while deque:
            status, step = deque.popleft()
            for nextStats in get(status):
                if nextStats not in seen and nextStats not in deads:
                    if nextStats == target:
                        return step+1
                    deque.append((nextStats,step+1))
                    seen.add(nextStats)
        return -1

sol = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(sol.openLock(deadends,target))