from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(edge):
            if edge in visited:
                return 
            
            visited.add(edge)
            
            for neigh in graph[edge]:
                dfs(neigh)
        
        count = 0 
        for edge in range(n):
            if edge not in visited:
                dfs(edge)
                count += 1
        
        return count 
        