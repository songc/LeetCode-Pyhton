# 937. 重新排列日志文件
# 给你一个日志数组 logs。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 标识符 。

# 有两种不同类型的日志：

# 字母日志：除标识符之外，所有字均由小写字母组成
# 数字日志：除标识符之外，所有字均由数字组成
# 请按下述规则将日志重新排序：

# 所有 字母日志 都排在 数字日志 之前。
# 字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
# 数字日志 应该保留原来的相对顺序。
# 返回日志的最终顺序。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reorder-data-in-log-files
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpDict = dict()
        numList = []
        for log in logs:
            strList = log.split()
            if strList[1].isdigit():
                numList.append(log)
            else:
                alpDict[(" ".join(strList[1:]),strList[0])]=log
        ans = [alpDict[i] for i in sorted(alpDict.keys())]
        return ans+numList

sol = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(sol.reorderLogFiles(logs))