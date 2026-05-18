class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        time, fresh = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    x, y = dr + r, dc + c
                    if (x in range(ROWS) and y in range(COLS) and
                    grid[x][y] == 1):
                        grid[x][y] = 2
                        q.append((x, y))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
