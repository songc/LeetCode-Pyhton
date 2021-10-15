# 38. 外观数列
# 给定一个正整数 n ，输出外观数列的第 n 项。

# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

# 你可以将其视作是由递归公式定义的数字字符串序列：

# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-and-say
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def countAndSay(self, n: int) -> str:
        res = ["1","11","21","1211"]
        if n<=4:
            return res[n-1]
        def convert(s):
            s+="#"
            n = len(s)
            res = []
            left,right = 0,0
            while right<n:
                if s[right]!=s[left]:
                    res.append(str(right-left)+s[left])
                    left=right
                right+=1    
            return "".join(res)

        for i in range(4,n):
            res.append(convert(res[-1]))
        return res[-1]

sol = Solution()
print(sol.countAndSay(5))
            