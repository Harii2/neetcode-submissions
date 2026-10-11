from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = defaultdict(int)
        max_len = 0
        max_freq = 0 
        r, l = 0, 0 

        while r < len(s):
            count_map[s[r]] += 1 
            curr_char_count = count_map[s[r]]

            max_freq = max(max_freq, curr_char_count)

            while (r-l+1) - max_freq > k:
                count_map[s[l]] -= 1 
                l += 1 
            
            max_len = max(max_len, r-l+1)
            r += 1 
        return max_len
