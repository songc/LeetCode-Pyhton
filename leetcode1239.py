# 1239. 串联字符串的最大长度
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。

# 请返回所有可行解 s 中最长长度。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        n = len(arr)
        for i in range(n):
            sa = set(arr[i])
            if len(sa) < len(arr[i]):
                continue
            tmp = []
            for s in dp:
                if sa.intersection(s):
                    continue
                tmp.append(sa.union(s))
                if len(tmp[-1]) == 26:
                    return 26
            dp += tmp
        ans = 0
        for s in dp:
            ans = max(ans, len(s))
        return ans


sol = Solution()
# arr = ["un", "iq", "ue"]
arr = ["yy","bkhwmpbiisbldzknpm"]
# arr = ["cha","r","act","ers"]
print(sol.maxLength(arr))
