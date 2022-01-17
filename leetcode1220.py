# 1220. 统计元音字母序列的数目
# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：

# 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
# 每个元音 'a' 后面都只能跟着 'e'
# 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
# 每个元音 'i' 后面 不能 再跟着另一个 'i'
# 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
# 每个元音 'u' 后面只能跟着 'a'
# 由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-vowels-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    def countVowelPermutation(self, n: int) -> int:
        Mod = 10**9+7
        dp=[1,1,1,1,1]
        for i in range(1,n):
            tmp = []
            for j in range(5):
                if j==0:
                    num = dp[1]+dp[4]+dp[2]
                elif j==1:
                    num = dp[0]+dp[2]
                elif j==2:
                    num = dp[1]+dp[3]
                elif j==3:
                    num = dp[2]
                elif j==4:
                    num = dp[2]+dp[3]
                tmp.append(num%Mod)
            dp=tmp
        return sum(dp)%Mod
    
sol = Solution()
print(sol.countVowelPermutation(5))
