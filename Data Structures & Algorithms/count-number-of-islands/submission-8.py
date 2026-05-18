class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0
        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i,j))
            while q:
                r, c = q.popleft()
                directions = [[-1,0], [1,0], [0,1], [0,-1]]
                for x, y in directions:
                    dr, dc = x + r, y + c 
                    if ((dr in range(ROWS)) and (dc in range(COLS)) and 
                        (grid[dr][dc] == "1") and (dr, dc) not in visited):
                        q.append((dr, dc))
                        visited.add((dr,dc))

        for i in range(ROWS):
            for j in range(COLS):
                if (grid[i][j] == "1" and (i,j) not in visited):
                    bfs(i, j)
                    islands += 1

        return islands