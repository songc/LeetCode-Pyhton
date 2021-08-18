# 552. 学生出勤记录 II
# 可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

# 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
# 给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 109 + 7 取余 的结果。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/student-attendance-record-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9+7
        if n ==1:
            return 3
        # dp的0，1，2 为 不缺勤，最后连续0，1，2天迟到，3，4，5为缺勤1次，最后连续0，1，2天迟到的。
        dp = [1,1,0,1,0,0]
        for i in range(2,n+1):
            newDp = [0]*6
            newDp[0]=(dp[0]+dp[1]+dp[2])%mod
            newDp[1]=(dp[0])%mod
            newDp[2]=(dp[1])%mod
            newDp[3]=(dp[0]+dp[1]+dp[2]+dp[3]+dp[4]+dp[5])%mod
            newDp[4]=(dp[3])%mod
            newDp[5]=(dp[4])%mod
            dp = newDp
        return sum(dp)%mod

sol = Solution()
print(sol.checkRecord(10101))

