class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        rowDups = defaultdict(set)
        colDups = defaultdict(set)
        miniDups = defaultdict(set)
        
        for i in range(ROWS):
            for j in range(COLS): 
                val = board[i][j] 
                key = (i // 3, j // 3)
                if val == ".":
                    continue 
                if val in rowDups[i] or val in colDups[j] or val in miniDups[key]:
                    return False
                rowDups[i].add(val)
                colDups[j].add(val)
                miniDups[key].add(val)
        
        return True
                