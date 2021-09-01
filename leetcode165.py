# 165. 比较版本号
# 给你两个版本号 version1 和 version2 ，请你比较它们。

# 版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。

# 比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。

# 返回规则如下：

# 如果 version1 > version2 返回 1，
# 如果 version1 < version2 返回 -1，
# 除此之外返回 0。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/compare-version-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        if len(v1)>len(v2):
            for i in range(len(v1)-len(v2)):
                v2.append(0)
        if len(v2)>len(v1):
            for i in range(len(v2)-len(v1)):
                v1.append(0)
        if v1 == v2:
            return 0
        elif v1<v2:
            return -1
        else:
            return 1

class Solution2:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1,v2 in zip_longest(version1.split('.'),version2.split('.'),fillvalue=0):
            x,y = int(v1),int(v2)
            if x!=y:
                return -1 if x<y else 1
        return 0



version1 = "1.11"
version2 = "1.001"
sol = Solution2()
print(sol.compareVersion(version1,version2))