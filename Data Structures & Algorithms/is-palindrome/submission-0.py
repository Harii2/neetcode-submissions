class Solution:
    def isPalindrome(self, s: str) -> bool:

        final_s = ""
        for ch in s:
            if ch.isalnum() : 
                final_s += ch


        i, j = 0, len(final_s)-1


        final_s = final_s.lower()
        print(final_s)
        while i<j:
            if final_s[i] != final_s[j]:
                return False 
            
            i += 1 
            j -= 1 
        
        return True

        