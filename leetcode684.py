import collections
class Solution:
    def findRedundantConnection(self, edges: list) -> list:
        v = set()
        for v1, v2 in edges:
            v.add(v1)
            v.add(v2)
        visited=set(edges[0])
        queue = collections.deque([])
        queue.extend(edges[1:])
        while queue:
            v1, v2 = queue.popleft()
            if v1 in visited and v2 in visited:
                if visited==v:
                    return [v1,v2]
                else:
                    queue.append([v1,v2])
            elif v1 in visited or v2 in visited:
                visited.add(v1)
                visited.add(v2)
            elif v1 not in visited and v2 not in visited:
                queue.append([v1,v2])
        

sol=Solution()
edges=[[3,4],[1,2],[2,4],[3,5],[2,5]]
print(sol.findRedundantConnection(edges))
        
        
