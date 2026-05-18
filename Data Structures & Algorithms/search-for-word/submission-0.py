class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #if word starts with char pos, then check horizontal and vertical nodes
        #cant revist the same node within a path --> set
        #Base Case: if we finish entire word, return true
        #Base Case: if row < 0 or c < 0 or r >= ROWS
        #           or c >= COLS or wrong character
        #           or visited same node, return False
        #recursive dfs, on all 4 adjacent position, if any return true, res returns true
        #remove pos from path
        #go thru every pos in grid and run dfs
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS 
                or c >= COLS or word[i] != board[r][c]
                or (r,c) in path):
                return False
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            path.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False

