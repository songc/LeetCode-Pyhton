# 1374. 生成每种字符都是奇数个的字符串
# 给你一个整数 n，请你返回一个含 n 个字符的字符串，其中每种字符在该字符串中都恰好出现 奇数次 。

# 返回的字符串必须只含小写英文字母。如果存在多个满足题目要求的字符串，则返回其中任意一个即可。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/generate-a-string-with-characters-that-have-odd-counts
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            return "a"+"b"*(n-1)
        else:
            return "a"*n
