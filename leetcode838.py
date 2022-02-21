# 838. 推多米诺
# n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。

# 每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

# 如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。

# 就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。

# 给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：

# dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
# dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
# dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
# 返回表示最终状态的字符串。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/push-dominoes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



import collections


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        visited= set()
        ans = []
        lset = set()
        rset = set()
        for i in range(len(dominoes)):
            if dominoes[i]=="L":
                lset.add(i)
                visited.add(i)
            if dominoes[i]=="R":
                rset.add(i)
                visited.add(i)
            ans.append(dominoes[i])
        while lset or rset:
            tmpL = set()
            for i in lset:
                if i-1>=0 and i-1 not in visited:
                    tmpL.add(i-1)
                    ans[i-1]="L"
            tmpR = set()
            for i in rset:
                if i+1<len(dominoes) and i+1 not in visited:
                    if i+1 in tmpL:
                        ans[i+1]="."
                    else:
                        ans[i+1]="R"
                        tmpR.add(i+1)
            visited.update(tmpL)
            visited.update(tmpR)
            lset=tmpL
            rset=tmpR
        return "".join(ans)

sol = Solution()
dominoes = "RR.L"
print(sol.pushDominoes(dominoes))
