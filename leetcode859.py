# 859. 亲密字符串
# 给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。

# 交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。

# 例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/buddy-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        sn = len(s)
        gn = len(goal)
        if sn!=gn:
            return False
        diffInd = []
        for i in range(sn):
            if s[i] !=goal[i]:
                diffInd.append(i)
                if len(diffInd)>=3:
                    return False
        if len(diffInd)==2:
            if s[diffInd[0]]==goal[diffInd[1]] and s[diffInd[1]]==goal[diffInd[0]]:
                return True
            else:
                return False
        elif len(diffInd)==1:
            return False
        else:
            return sn>len(set(s))

sol = Solution()
s = "ab"
goal = "ab"
print(sol.buddyStrings(s,goal))