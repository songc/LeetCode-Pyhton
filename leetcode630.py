# 630. 课程表 III
# 这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。

# 你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。

# 返回你最多可以修读的课程数目。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/course-schedule-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        q=list()
        total=0
        for ti,di in courses:
            if total+ti<=di:
                total+=ti
                heapq.heappush(q,-ti)
            elif q and -q[0]>ti:
                total-=-q[0]-ti
                heapq.heappop(q)
                heapq.heappush(q,-ti)
        return len(q)


sol = Solution()
courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
print(sol.scheduleCourse(courses))
                

