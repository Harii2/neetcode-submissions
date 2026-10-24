import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-each for each in nums]
        heapq.heapify(nums)

        while k:
            val = heapq.heappop(nums)
            k -= 1 
        
        return - val

        