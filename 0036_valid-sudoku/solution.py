from typing import List

# Time : Beats 100.0 %
# Memo : Beats 69.51 %
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_box = [set() for x in range(9)]
        check_col = [set() for x in range(9)]

        for r in range(9):
            check_row = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in check_row: 
                    return False
                if board[r][c] in check_col[c]: 
                    return False
                b = r//3*3 + c//3
                if board[r][c] in check_box[b]:
                    return False
                
                check_row.add(board[r][c])
                check_col[c].add(board[r][c])
                check_box[b].add(board[r][c])

        return True
        
        