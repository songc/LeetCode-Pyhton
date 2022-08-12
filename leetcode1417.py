# 1417. 重新格式化字符串
# 给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。

# 请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。

# 请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/reformat-the-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



from itertools import zip_longest


class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        chars = []
        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                chars.append(c)
        n = len(nums)
        n2 = len(chars)
        if abs(n-n2)>1:
            return ''
        if n2>n:
            nums,chars = chars,nums
        ans = []
        for i,j in zip_longest(nums,chars):
            ans.append(i)
            if j:
                ans.append(j)
        return "".join(ans)