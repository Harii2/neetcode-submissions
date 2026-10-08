class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def return_empty_set():
            return [set() for _ in range(9)]
        rows = return_empty_set()
        cols = return_empty_set()
        squares = return_empty_set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue 
                
                num = board[i][j]

                square_index = (i//3) * 3 + (j // 3)
                is_alread_existed = num in cols[j] or num in rows[i] or num in squares[square_index]

                if is_alread_existed:
                    return False 
                
                rows[i].add(num)
                cols[j].add(num)
                squares[square_index].add(num)
        
        return True 
                
