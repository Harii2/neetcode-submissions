class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        seen = set()

        max_len = 0
        for num in nums:
            if num in seen:
                continue 
            
            curr_len = 1 
            while num + 1 in num_set:
                num += 1 
                seen.add(num)
                curr_len += 1
            max_len = max(curr_len, max_len)
            
            seen.add(num)
        
        return max_len