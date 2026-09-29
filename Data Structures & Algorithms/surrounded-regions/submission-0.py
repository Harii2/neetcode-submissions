class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            if board[r][c] != "O": 
                return

            visited.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] == "O"
                ):
                    dfs(nr, nc, visited)

        visited = set()

        # Top + bottom
        for c in range(cols):
            dfs(0, c, visited)
            dfs(rows - 1, c, visited)

        # Left + right
        for r in range(rows):
            dfs(r, 0, visited)
            dfs(r, cols - 1, visited)

        # Convert surrounded O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'