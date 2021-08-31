# 1109. 航班预订统计
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。

# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

# 请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/corporate-flight-bookings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import bisect

# 超时
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for first,last,seats in bookings:
            for i in range(first-1,last):
                res[i]+=seats
        return res
# 解题思路：
# 换一种思路理解题意，将问题转换为：某公交车共有 n 站，第 i 条记录 bookings[i] = [i, j, k] 表示在 i 站上车 k 人，乘坐到 j 站，在 j+1 站下车，需要按照车站顺序返回每一站车上的人数
# 根据 1 的思路，定义 counter[] 数组记录每站的人数变化，counter[i] 表示第 i+1 站。遍历 bookings[]：bookings[i] = [i, j, k] 表示在 i 站增加 k 人即 counters[i-1] += k，在 j+1 站减少 k 人即 counters[j] -= k
# 遍历（整理）counter[] 数组，得到每站总人数： 每站的人数为前一站人数加上当前人数变化 counters[i] += counters[i - 1]

# 作者：LuoRong1994
# 链接：https://leetcode-cn.com/problems/corporate-flight-bookings/solution/5118_hang-ban-yu-ding-tong-ji-by-user9081a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution2:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for first,last,seats in bookings:
            res[first-1]+=seats
            if last <n:
                res[last]-=seats
        for i in range(1,n):
            res[i]+=res[i-1]
        return res


sol = Solution2()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(sol.corpFlightBookings(bookings,n))