class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        l, r = 0, 0 

        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1 

            seen.add(s[r])
            r += 1 
            max_len = max(max_len, r-l)

        return max_len