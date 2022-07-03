# 556. 下一个更大元素 III
# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

# 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/next-greater-element-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        c = list(str(n))
        tmpMax = 2**31
        for i in range(len(c)-1,-1,-1):
            for j in range(len(c)-1,i,-1):
                if c[i]<c[j]:
                    c[i],c[j]=c[j],c[i]
                    ans =  int("".join(c[:i+1]+sorted(c[i+1:])))
                    if ans<tmpMax:
                        return ans
                    return -1
        return -1

sol = Solution()
n=2147483486
print(sol.nextGreaterElement(n))