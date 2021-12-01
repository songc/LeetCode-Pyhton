# 1723. 完成所有工作的最短时间
# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。

# 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。

# 返回分配方案中尽可能 最小 的 最大工作时间 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 暴力搜索，超时
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        klist = [0]*k
        klist.reverse()
        res = sum(jobs)
        def backtract(ind):
            nonlocal res
            if ind == len(jobs):
                res=min(res,max(klist))
                return
            for i in range(len(klist)):
                klist[i]+=jobs[ind]
                backtract(ind+1)
                klist[i]-=jobs[ind]
        backtract(0)
        return res

#回溯+剪枝
class Solution2:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        klist = [0]*k
        jobs.sort()
        jobs.reverse()
        res = sum(jobs)
        def backtract(ind,userInd,tmpMax):
            nonlocal res
            if tmpMax>=res:
                return
            if ind == len(jobs):
                res=tmpMax
                return
            if userInd<k:
                klist[userInd]+=jobs[ind]
                nextMax = max(tmpMax,klist[userInd])
                backtract(ind+1,userInd+1,nextMax)
                klist[userInd]-=jobs[ind]
            # 注意这里的循环范围是userInd
            for i in range(userInd):
                klist[i]+=jobs[ind]
                nextTmpMax = max(tmpMax,klist[i])
                backtract(ind+1, userInd ,nextTmpMax)
                klist[i]-=jobs[ind]
        backtract(0,0,0)
        return res

sol = Solution2()
jobs = [1,2,4,7,8]
k = 2
print(sol.minimumTimeRequired(jobs,k))
            