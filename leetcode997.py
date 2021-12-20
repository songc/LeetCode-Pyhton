# 997. 找到小镇的法官
# 在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。

# 如果小镇的法官真的存在，那么：

# 小镇的法官不相信任何人。
# 每个人（除了小镇法官外）都信任小镇的法官。
# 只有一个人同时满足条件 1 和条件 2 。
# 给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。

# 如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-the-town-judge
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        vset1=set()
        vDict = dict()
        for i,j in trust:
            vset1.add(i)
            if j in vDict:
                vDict[j]+=1
            else:
                vDict[j]=1
        vset = set(vDict.keys())-vset1
        if len(vset)==1:
            key = list(vset)[0]
            if vDict[key]== n-1:
                return key
        return -1