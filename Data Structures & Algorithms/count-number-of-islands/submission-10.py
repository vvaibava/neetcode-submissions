class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q: 
                x,y = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    a, b = x + dr, y + dc
                    if a in range(ROWS) and b in range(COLS) and grid[a][b] == '1' and (a,b) not in visit:
                        q.append((a,b))
                        visit.add((a,b)) 

        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == '1' and (r,c) not in visit):
                    bfs(r,c)
                    count += 1
        return count