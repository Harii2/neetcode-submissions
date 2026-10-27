class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 1 
        index = len(digits) - 1
        while count and index >= 0:
            add_val = digits[index] + count 
            digits[index] = add_val % 10 
            
            count = add_val // 10 
            index -= 1
        
        if count:
            digits.insert(0, count)
        return digits
        