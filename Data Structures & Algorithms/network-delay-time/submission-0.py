import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        dist = [float("inf")]* (n+1)
        dist[k] = 0 
        heap = [(0, k)]

        while heap:
            curr_time, node = heapq.heappop(heap)

            for neigh, time in graph[node]:
                new_time = curr_time + time 
                if new_time < dist[neigh]:
                    dist[neigh] = new_time 
                    heapq.heappush(heap, (new_time, neigh))
        
        for i in range(1, n+1):
            if dist[i] == float("inf"):
                return -1 
        
        return max(dist[1:])


