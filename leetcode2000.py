# 2000. 反转单词前缀
# 给你一个下标从 0 开始的字符串 word 和一个字符 ch 。找出 ch 第一次出现的下标 i ，反转 word 中从下标 0 开始、直到下标 i 结束（含下标 i ）的那段字符。如果 word 中不存在字符 ch ，则无需进行任何操作。

# 例如，如果 word = "abcdefd" 且 ch = "d" ，那么你应该 反转 从下标 0 开始、直到下标 3 结束（含下标 3 ）。结果字符串将会是 "dcbaefd" 。
# 返回 结果字符串 。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-prefix-of-word
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = word.find(ch)
        if ind > 0:
            return word[ind::-1] + word[ind + 1 :]
        return word


sol = Solution()
word = "abcdefd"
ch = "d"
print(sol.reversePrefix(word, ch))
