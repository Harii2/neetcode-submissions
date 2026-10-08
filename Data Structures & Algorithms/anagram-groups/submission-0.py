class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for word in strs:
            cnt_arr = [0]*26 
            for ch in word:
                cnt_arr[ord(ch) - ord('a')] += 1 
            
            key = tuple(cnt_arr)
            if key in grp:
                grp[key].append(word)
            else:
                grp[key] = [word]
        
        return [
            list(values)
            for key, values in grp.items()
        ]
        