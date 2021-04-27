# 1011. 在 D 天内送达包裹的能力
# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
# 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left,right = max(weights), sum(weights)
        while left<right:
            mid = left+(right-left)//2
            need,curr= 1,0
            for w in weights:
                curr += w
                if curr>mid:
                    curr=w
                    need+=1
            if need>D:
                left=mid+1
            else:
                right=mid
        return left

sol = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(sol.shipWithinDays(weights,D))

