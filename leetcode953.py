# 953. 验证外星语词典
# 某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

# 给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/verifying-an-alien-dictionary
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = dict( (v,ind) for ind, v in enumerate(order))
        n = len(words)
        pre = [order[i] for i in words[0]]
        for i in range(1,n):
            new = [order[j] for j in words[i]]
            if new<pre:
                return False
            pre = new
        return True

sol = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(sol.isAlienSorted(words,order))
