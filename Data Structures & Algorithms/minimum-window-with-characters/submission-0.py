from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_map = defaultdict(int)
        for ch in t:
            t_map[ch] += 1 
        
        have = 0 
        need = len(t_map)
        min_len = float("inf")
        result = ""

        l, r = 0, 0
        window = defaultdict(int)
        while r < len(s):
            window[s[r]] += 1 
            if window[s[r]] == t_map[s[r]]:
                have += 1 
            
            while have == need:
                if r-l+1 < min_len:
                    min_len = r-l+1 
                    result = s[l:r+1]
                
                window[s[l]] -= 1 
                if window[s[l]] < t_map[s[l]]:
                    have -= 1 
                l += 1

            r += 1 
        return result

