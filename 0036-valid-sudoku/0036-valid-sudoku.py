
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
        
        # defaultdict(<class 'set'>, {(0, 0): set(), 0: {'6', '9', '5', '8', '3'}, (0, 1): set(), 1: {'1', '9', '5', '4', '7', '8'}, (0, 2): set(), 2: {'6', '3', '2', '8'}, (1, 0): set(), (1, 1): set(), (1, 2): set(), 3: {'1', '6', '9', '4', '8', '3'}, (2, 0): set(), (2, 2): set(), 4: {'2', '9', '5', '7', '8'}, (2, 1): set()})
