class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return 0
            if j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0 
            
            grid[i][j] = 0
            
            return (
                1 
                + dfs(i-1, j)
                + dfs(i+1, j)
                + dfs(i, j-1)
                + dfs(i, j+1)
            )

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = dfs(i, j)
                    max_area = max(
                        curr_area, max_area
                    )
        return max_area
        