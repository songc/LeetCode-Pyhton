# 1694. 重新格式化电话号码
# 给你一个字符串形式的电话号码 number 。number 由数字、空格 ' '、和破折号 '-' 组成。

# 请你按下述方式重新格式化电话号码。

# 首先，删除 所有的空格和破折号。
# 其次，将数组从左到右 每 3 个一组 分块，直到 剩下 4 个或更少数字。剩下的数字将按下述规定再分块：
# 2 个数字：单个含 2 个数字的块。
# 3 个数字：单个含 3 个数字的块。
# 4 个数字：两个分别含 2 个数字的块。
# 最后用破折号将这些块连接起来。注意，重新格式化过程中 不应该 生成仅含 1 个数字的块，并且 最多 生成两个含 2 个数字的块。

# 返回格式化后的电话号码。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/reformat-phone-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def reformatNumber(self, number: str) -> str:
        ans = []
        tmp = []
        for c in number:
            if c.isdigit():
                tmp.append(c)
                if len(tmp)==3:
                    ans.append("".join(tmp))
                    tmp=[]
        if len(tmp)==1:
            t = ans.pop()
            ans.append(t[:-1])
            ans.append(t[-1]+tmp[0])
        if len(tmp)==2:
            ans.append("".join(tmp))
        return "-".join(ans)

sol = Solution()
number = "123 4-567"
print(sol.reformatNumber(number))
            

    