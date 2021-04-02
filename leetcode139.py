# 139. 单词拆分
# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

# 说明：

# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-break
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0]=True
        tmpSet = set(wordDict)
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i] and (s[i:j] in tmpSet):
                    dp[j]=True
        return dp[-1]
            