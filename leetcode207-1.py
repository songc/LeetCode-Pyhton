import collections
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for val1, val2 in prerequisites:
            edges[val2].append(val1)
            indegree[val1]+=1

        deque = collections.deque()
        for i in range(numCourses):
            if i not in indegree:
                deque.append(i)
        visited = 0
        while deque:
            val = deque.popleft()
            visited+=1
            for j in edges[val]:
                indegree[j]-=1
                if indegree[j]==0:
                    deque.append(j)
        return visited==numCourses