class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        candidates.sort()

        def backtrack(index, remaining):
            if remaining == 0:
                result.append(current.copy())
                return 
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue 
                
                if candidates[i] > remaining:
                    break 
                
                current.append(
                    candidates[i]
                )
                backtrack(
                    i+1, remaining-candidates[i]
                )
                current.pop()
            
        
        backtrack(0, target)
        return result 

        