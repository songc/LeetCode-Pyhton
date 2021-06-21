# 401. 二进制手表
# 二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。

# 例如，下面的二进制手表读取 "3:25" 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-watch
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。

# 小时不会以零开头：

# 例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
# 分钟必须由两位数组成，可能会以零开头：

# 例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range(5):
            j = turnedOn-i
            if j<=6:
                h = self.getAllNum(11,i)
                m = self.getAllNum(59,j)
                for hi in h:
                    for mi in m:
                        res.append(str(hi)+":"+"{:0=2d}".format(mi))
        return res


    def getAllNum(self, maxNum ,count):
        res = []
        for i in range(maxNum+1):
            if bin(i).count("1")==count:
                res.append(i)
        return res

sol = Solution()
print(sol.readBinaryWatch(6))     