# 804. 唯一摩尔斯密码词
# 国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 比如:

# 'a' 对应 ".-" ，
# 'b' 对应 "-..." ，
# 'c' 对应 "-.-." ，以此类推。
# 为了方便，所有 26 个英文字母的摩尔斯密码表如下：

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-morse-code-words
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dictList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        vset = set()
        for word in words:
            tmp = []
            for ch in word:
                tmp.append(dictList[ord(ch)-ord('a')])
            vset.add("".join(tmp))
        return len(vset)

sol = Solution()
words = ["gin", "zen", "gig", "msg"]
print(sol.uniqueMorseRepresentations(words))