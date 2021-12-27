# 1154. 一年中的第几天
# 给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。

# 通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/day-of-the-year
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def dayOfYear(self, date: str) -> int:
        strList = date.split("-")
        mouthDays = [31,29,31,30,31,30,31,31,30,31,30,31]
        year = int(strList[0])
        month = int(strList[1])
        days = int(strList[2])
        flag = False
        if year%100==0:
            if year%400==0:
                flag=True
        elif year%4==0:
            flag=True
        res = sum(mouthDays[:month-1])+days
        if flag:
            return res
        return res if month<=2 else res-1

class Solution2:
    def dayOfYear(self, date: str) -> int:
        strList = date.split("-")
        mouthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
        year = int(strList[0])
        month = int(strList[1])
        days = int(strList[2])
        if year%100==0:
            if year%400==0:
                mouthDays[1]+=1
        elif year%4==0:
            mouthDays[1]+=1
        return sum(mouthDays[:month-1])+days


sol = Solution2()
date = "2003-03-01"
print(sol.dayOfYear(date))
