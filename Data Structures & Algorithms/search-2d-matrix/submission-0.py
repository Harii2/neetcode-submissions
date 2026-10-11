class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, (len(matrix) * len(matrix[0])) -1 

        rows = len(matrix)
        cols = len(matrix[0])


        while l <= r:
            mid = (l + r) // 2 
            row = mid // cols
            c = mid % cols 
            if matrix[row][c] == target:
                return True 
            elif matrix[row][c] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False 


        