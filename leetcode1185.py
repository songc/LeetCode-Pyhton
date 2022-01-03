# 1185. 一周中的第几天
# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

# 输入为三个整数：day、month 和 year，分别表示日、月、年。

# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/day-of-the-week
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekStr = ["Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        yearsDay = 365*3+366
        monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
        div,mod = divmod(year-1971,4)
        days = yearsDay*div
        if (year%4==0 and year%100!=0) or year%400==0:
            monthDays[1]+=1
        if mod >1:
            days+=365*(mod-1)+366
        elif mod ==1 :
            days+=365
        days=days+sum(monthDays[:month-1])+day-1
        return weekStr[days%7]

sol = Solution()
day = 31
month = 8
year = 2100
print(sol.dayOfTheWeek(day,month,year))