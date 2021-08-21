# 443. 压缩字符串

# 给你一个字符数组 chars ，请使用下述算法压缩：

# 从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

# 如果这一组长度为 1 ，则将字符追加到 s 中。
# 否则，需要向 s 追加字符，后跟这一组的长度。
# 压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

# 请在 修改完输入数组后 ，返回该数组的新长度。

# 你必须设计并实现一个只使用常量额外空间的算法来解决此问题。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/string-compression
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n<=1:
            return n
        s = chars[0]
        curr = 1
        tmp = 1
        while curr<n:
            if chars[curr]==s[-1]:
                tmp+=1
            else:
                if tmp>1:
                    s+=str(tmp)
                s+=chars[curr]
                tmp=1
            curr+=1
        if tmp>1:
            s+=str(tmp)
        n = len(s)
        for i in range(n):
            chars[i]=s[i]
        return n


class Solution2:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n<=1:
            return n
        curr = 0
        writer = 0
        while curr<n:
            start = curr
            while curr<n-1 and chars[curr]==chars[curr+1]:
                curr+=1
            num = curr-start+1
            chars[writer]=chars[start]
            writer+=1
            if num>1:
                snum = str(num)
                for s in snum:
                    chars[writer]=s
                    writer+=1
            curr+=1
        return writer


sol = Solution2()
chars = ["a","a","b","b","c","c","c"]
print(sol.compress(chars))


        