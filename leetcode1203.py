import collections
class Solution:
    def sortItems(self, n: int, m: int, group: list, beforeItems: list) -> list:
        max_m = m
        for i in range(n):
            if group[i]==-1:
                group[i]=max_m
                max_m+=1

        taskIndegree = [0]*n
        groupIndegree = [0]*max_m
        taskNeighbors = [[] for _ in range(n)]
        groupNeighbors = [[] for _ in range(max_m)]
        group_task=[[] for _ in range(max_m)]
        for ind,items in enumerate(beforeItems):
            group_task[group[ind]].append(ind)
            if items:                
                for item in items:
                    if group[ind] != group[item]:
                        groupIndegree[group[ind]] +=1
                        groupNeighbors[group[item]].append(group[ind])
                    else:
                        taskIndegree[ind]+=1
                        taskNeighbors[item].append(ind)
        gr = [i for i in range(max_m)]
        group_queue_list = self.sort_queue(gr, groupIndegree, groupNeighbors)
        res=[]
        if len(group_queue_list) != max_m:
            return res
        for  group_queue in group_queue_list:
            task_queue = self.sort_queue(group_task[group_queue],taskIndegree, taskNeighbors)
            if len(task_queue) != len(group_task[group_queue]):
                return []
            res+=task_queue
        return res
    def sort_queue(self, tasks:list, taskIndgree:list, taskNeighbors:list):
        res =[]
        queue = collections.deque([])
        for task in tasks:
            if taskIndgree[task]==0:
                queue.append(task)
        while queue:
            cur=queue.popleft()
            res.append(cur)
            for nei in taskNeighbors[cur]:
                taskIndgree[nei]-=1
                if taskIndgree[nei]==0:
                    queue.append(nei)
        return res

sol = Solution()
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
print(sol.sortItems(n,m,group,beforeItems))