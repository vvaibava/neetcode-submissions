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
            q.append((i,j))
            visited.add((i,j))
            directions = [[-1,0], [1,0], [0,1], [0,-1]]
            count = 1
            while q:
                r, c = q.popleft()
                for x, y in directions:
                    dr, dc = x + r, c + y
                    if (dr in range(ROWS) and dc in range(COLS)
                        and grid[dr][dc] == 1 and (dr,dc) not in visited):
                        q.append((dr,dc))
                        visited.add((dr,dc))
                        count += 1
            return count
                    

        for i in range(ROWS):
            for j in range(COLS):
                if (grid[i][j] == 1 and (i,j) not in visited):
                    currArea = bfs(i,j)
                    area = max(area, currArea)
        return area