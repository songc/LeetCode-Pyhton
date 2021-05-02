"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        edict = dict()
        for e in employees:
            edict[e.id]=e
        ans=0
        def dfs(eid):
            nonlocal ans
            ans+=edict[eid].importance
            for newEid in edict[eid].subordinates:
                dfs(newEid)
        dfs(id)
        return ans

# sol = Solution()
# employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
# id = 1
# print(sol.getImportance(employees,id))