class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_size = len(board[0])
        
        rule01 = False
        count_01 = 0

        rule02 = [False] * row_size
        rule03 = [False] * row_size

        for i in range(len(board)):
            
            for j in range(row_size):
                if board[i][j] is not ".":
                    rule01 = True
                    rule02[j] = True
        
            if rule01: 
                rule01 = False
                count_01 += 1
        
        return count_01 == row_size and [True] * row_size == rule02
