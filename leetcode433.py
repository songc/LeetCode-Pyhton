# 433. 最小基因变化
# 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。

# 假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

# 例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
# 另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。

# 给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。

# 注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-genetic-mutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bankSet = set(bank)
        deque = list()
        if end not in bankSet:
            return -1
        if start == end:
            return 0
        
        def getNewDeque(queue):
            newDeque = []
            for st, step in queue:
                for target in bankSet:
                    diff = 0
                    for i in range(8):
                        if st[i]!=target[i]:
                            diff+=1
                    if diff==1:
                        newDeque.append((target,step+1))
            return newDeque
        deque.append((start,0))        
        while deque:
            for st,step in deque:
                if st == end:
                    return step
            deque = getNewDeque(deque)
        return -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bankSet = set(bank)
        deque = list()
        if end not in bankSet:
            return -1
        if start == end:
            return 0
        
        def getNewDeque(queue):
            newDeque = []
            for st, step in queue:
                for target in bankSet:
                    if target in visited:
                        continue
                    diff = 0
                    for i in range(8):
                        if st[i]!=target[i]:
                            diff+=1
                    if diff==1:
                        newDeque.append((target,step+1))
                        visited.add(target)
            return newDeque
        visited = set()
        deque.append((start,0))        
        while deque:
            for st,step in deque:
                if st == end:
                    return step
            deque = getNewDeque(deque)
        return -1

sol = Solution()
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]


print(sol.minMutation(start,end,bank))
