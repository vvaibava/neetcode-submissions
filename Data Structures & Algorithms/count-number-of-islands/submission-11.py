class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = deque() 
            q.append((r,c))
            visited.add((r,c))
            while q: 
                x,y = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions: 
                    a, b = x + dr, y + dc
                    if a in range(ROWS) and b in range(COLS) and grid[a][b] == "1" and (a,b) not in visited:
                        q.append((a,b))
                        visited.add((a,b))


        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands