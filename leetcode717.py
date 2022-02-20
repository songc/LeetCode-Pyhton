# 717. 1比特与2比特字符
# 有两种特殊字符：

# 第一种字符可以用一个比特 0 来表示
# 第二种字符可以用两个比特(10 或 11)来表示、
# 给定一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一位字符，则返回 true 。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i=0
        while i<n:
            if i==n-1:
                return True
            if bits[i]==0:
                i+=1
            if bits[i]==1:
                i+=2
        return False

sol = Solution()
bits = [1, 1, 1, 0]
print(sol.isOneBitCharacter(bits))