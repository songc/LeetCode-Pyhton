# 761. 特殊的二进制序列
# 特殊的二进制序列是具有以下两个性质的二进制序列：

# 0 的数量与 1 的数量相等。
# 二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。
# 给定一个特殊的二进制序列 S，以字符串形式表示。定义一个操作 为首先选择 S 的两个连续且非空的特殊的子串，然后将它们交换。（两个子串为连续的当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。)

# 在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/special-binary-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s)<=2:
            return s
        cur = left = 0
        subList = []
        for i,ch in enumerate(s):
            if ch=="1":
                cur+=1
            else:
                cur-=1
                if cur==0:
                    subList.append("1{}0".format(self.makeLargestSpecial(s[left+1:i])))
                    left=i+1
        subList.sort(reverse=True)
        return "".join(subList)

sol = Solution()
s = "11011000"
print(sol.makeLargestSpecial(s))
