# 781. 森林中的兔子
# 森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。

# 返回森林中兔子的最少数量。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rabbits-in-forest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import math
import collections
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        counter = collections.Counter(answers)
        for k in counter:
            if k==0:
                ans +=counter[k]
            else:
                ans += math.ceil(counter[k]/(k+1))*(k+1)
        return ans

sol = Solution()
answers = [10,10,10]
print(sol.numRabbits(answers))