from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 :
                    queue.append((i, j))
        
        level = 0 
        while queue:
            level += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()

                directions = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, +1)
                ]
                for di, dj in directions:
                    ni = i + di 
                    nj = j + dj 
                    if (
                        0 <= ni < len(grid) and 
                        0 <= nj < len(grid[0]) and 
                        grid[ni][nj] != -1 and 
                        grid[ni][nj] == 2147483647
                    ):
                        grid[ni][nj] = level
                        queue.append(
                            (ni, nj)
                        )
