# 207. 课程表
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/course-schedule
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict1 = collections.defaultdict(set)
        dict2 = collections.defaultdict(set)
        for val1,val2 in prerequisites:
            dict1[val1].add(val2)
            dict2[val2].add(val1)
        visited = set()
        def dfs(i):
            for j in dict2[i]:
                if j in visited:
                    continue
                if j not in dict1 or visited.issuperset(dict1[j]):
                    visited.add(j)
                    dfs(j)
        for i in range(numCourses):
            if i not in visited and i not in dict1:
                visited.add(i)
                dfs(i) 
        return len(visited)==numCourses