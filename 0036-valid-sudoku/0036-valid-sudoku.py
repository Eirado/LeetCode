
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows: defaultdict[int, set[str]] = defaultdict(set)
        colls: defaultdict[int, set[str]] = defaultdict(set)
        grid: defaultdict[int, set[str]] = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or 
                board[i][j] in colls[j] or 
                board[i][j] in grid[(i // 3, j // 3)]):
                    return False
                rows[i].add(board[i][j])
                colls[j].add(board[i][j])
                grid[(i // 3, j // 3)].add(board[i][j])
        return True
        
