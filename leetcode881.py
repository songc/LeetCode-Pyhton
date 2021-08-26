# 881. 救生艇

# 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

# 返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
from typing import List
import bisect

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left,right = 0,n-1
        res = 0
        while left<=right:
            if people[left]+people[right]<=limit:
                left+=1
            right-=1
            res+=1
        return res

sol = Solution()
people = [1,5,2,4]
limit = 6
print(sol.numRescueBoats(people,limit))     