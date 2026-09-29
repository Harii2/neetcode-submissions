class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [
            (0, 1), 
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, visited):
            visited.add((r,c))

            for dr, dc in directions:
                nr = r + dr 
                nc = c + dc 
                if (
                    0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    (nr, nc) not in visited and 
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)
        
        pacific = set()
        for c in range(COLS):
            dfs(0, c, pacific)
        
        for r in range(ROWS):
            dfs(r, 0, pacific)
        
        atlantic = set()
        for c in range(COLS):
            dfs(ROWS-1, c, atlantic)
        
        for r in range(ROWS):
            dfs(r, COLS-1, atlantic)
        
        return list(
            atlantic & pacific
        )
        




        