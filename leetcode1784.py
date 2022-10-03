# 1784. 检查二进制字符串字段
# 给你一个二进制字符串 s ，该字符串 不含前导零 。

# 如果 s 包含 零个或一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。

# 如果 s 中 由连续若干个 '1' 组成的字段 数量不超过 1，返回 true​​​ 。否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/check-if-binary-string-has-at-most-one-segment-of-ones
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count =0
        for c in s:
            if c=='1' and count>0:
                return False
            if c=='0':
                count+=1
        return True