from typing import List
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        area = 0

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            count = 1  # Start with the first cell

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS) and
                            grid[nr][nc] == 1 and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        count += 1
            return count

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    currArea = bfs(i, j)
                    area = max(area, currArea)

        return area
