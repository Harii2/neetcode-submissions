import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closest = []
        for p in points:
            distance = p[0]**2 + p[1]**2
            heapq.heappush(
                k_closest, (-distance, p)
            )
        
        while len(k_closest) > k:
            heapq.heappop(
                k_closest
            )
        
        return [ p for d, p in k_closest]
        