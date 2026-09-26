from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0 
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1 
        

        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                directions = [
                    (-1, 0),
                    (1, 0),
                    (0, 1),
                    (0, -1)
                ]
                for di, dj in directions:
                    ni = i + di 
                    nj = j + dj 
                    if (
                        0 <= ni < len(grid) and 
                        0 <= nj < len(grid[0]) and 
                        grid[ni][nj] == 1
                    ):
                        fresh -= 1 
                        grid[ni][nj] = 2 
                        queue.append(
                            (ni, nj)
                        )
            minutes += 1 
        if fresh > 0:
            return -1 
        return minutes

