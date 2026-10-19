class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(index, remaining):
            if remaining == 0:
                result.append(
                    current.copy()
                )
                return 
            
            if remaining < 0 or index == len(nums):
                return 
            
            current.append(
                nums[index]
            )
            backtrack(
                index, remaining-nums[index]
            )

            current.pop()
            backtrack(
                index+1, remaining
            )
        
        backtrack(0, target)
        return result 
        