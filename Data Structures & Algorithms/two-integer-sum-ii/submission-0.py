class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1 

        while left < right:
            sum_of_left_and_right = numbers[left] + numbers[right]
            if  sum_of_left_and_right == target:
                return [left+1, right+1]
            
            elif sum_of_left_and_right < target:
                left += 1 
            else:
                right -= 1 
        
        return [-1, -1]
            
            