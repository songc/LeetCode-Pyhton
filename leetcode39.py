# 39. 组合总和
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：

# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def combinationSum(self, candidates: list, target: int) -> List[List[int]]:
        sortedCandidate = sorted(candidates)
        ans = []
        def backtarck(nums, k):
            if k==0:
                ans.append(list(nums))
                return
            if k<0:
                return
            for i in sortedCandidate:
                if len(nums)>0 and i<nums[-1]:
                    continue
                nums.append(i)
                k-=i
                backtarck(nums,k)
                nums.pop()
                k+=i
        backtarck([],target)
        return ans