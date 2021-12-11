# 911. 在线选举
# 给你两个整数数组 persons 和 times 。在选举中，第 i 张票是在时刻为 times[i] 时投给候选人 persons[i] 的。

# 对于发生在时刻 t 的每个查询，需要找出在 t 时刻在选举中领先的候选人的编号。

# 在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。

# 实现 TopVotedCandidate 类：

# TopVotedCandidate(int[] persons, int[] times) 使用 persons 和 times 数组初始化对象。
# int q(int t) 根据前面描述的规则，返回在时刻 t 在选举中领先的候选人的编号。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/online-election
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
import bisect

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.res = []
        self.times = times
        n = len(times)
        pCount = collections.defaultdict(int)
        for i in range(n):
            pCount[persons[i]]+=1
            if self.res:
                if pCount[persons[i]]>=pCount[self.res[-1]]:
                    self.res.append((persons[i]))
                else:
                    self.res.append(self.res[-1])
            else:
                self.res.append(persons[i])


    def q(self, t: int) -> int:
        ind=bisect.bisect_right(self.times,t)
        return self.res[ind-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)