class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first binary search through num rows in matrix to find target row
        #check if target value is greater than largest value in row
        #if yes, bottom row is mid + 1, else top row is mid - 1, else break
        #if none of the rows have the target(!top <= bot) --> return false
        #get the target row and perform binary search on that row
 
        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW - 1
        while (top <= bot):
            row = (top + bot) // 2
            if (target > matrix[row][-1]):
                top = row + 1
            elif (target < matrix[row][0]):
                bot = row - 1
            else: 
                break
        
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        l, r = 0, COL - 1
        while (l <= r):
            m = (l + r) // 2
            if(target < matrix[row][m]):
                r = m - 1
            elif(target > matrix[row][m]):
                l = m + 1
            else: 
                return True
        return False