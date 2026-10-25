from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dfs(index):
            if index >= n-1:
                return 0 
            
            min_jumps = float("inf")
            for jump in range(1, nums[index]+1):
                steps = 1 + dfs(jump+index)
                min_jumps = min(
                    steps , min_jumps
                )

            return min_jumps
        
        return dfs(0)