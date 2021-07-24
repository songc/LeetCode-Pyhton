# 1736. 替换隐藏数字得到的最晚时间
# 给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。

# 有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。

# 替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maximumTime(self, time: str) -> str:
        h = 0
        m = 0
        if time[0]=="?":
            if time[1]=="?":
                h = 23
            elif int(time[1])<=3:
                h = 20+int(time[1])
            else:
                h = 10+int(time[1])
        elif time[1]=="?":
            if int(time[0])<2:
                h = int(time[0])*10+9
            else:
                h = 23
        else:
            h = int(time[:2])
        if time[3]=="?":
            if time[4]=="?":
                m = 59
            else:
                m = 50+int(time[4])
        elif time[4]=="?":
            m = int(time[3])*10+9
        else:
            m = int(time[-2:])
        return "{:0=2d}:{:0=2d}".format(h,m)

sol = Solution()
time = "2?:?0"
print(sol.maximumTime(time))
