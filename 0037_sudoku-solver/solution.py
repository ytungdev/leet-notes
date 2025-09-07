from typing import List
from collections import heapq

# Time : Beats 95.38 %
# Memo : Beats 60.63 %
# Backtracking DFS with heap
class Solution2:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        check_row = [set() for x in range(9)]
        check_col = [set() for x in range(9)]
        check_box = [set() for x in range(9)]
        # only check validity for specific cell
        def is_valid(r,c,b,d):
            if d in check_row[r]: return False  # noqa: E701
            if d in check_col[c]: return False  # noqa: E701
            if d in check_box[b]: return False  # noqa: E701
            return True

        # pre-order dfs with backtracking
        def solve(q):
            # Return True if done
            if not q:
                return True
            
            o,r,c = heapq.heappop(q)
            b = r//3*3 + c//3
            opt = 0
            # d is possible for board[r][c], then guess next with board[r][c]=d
            for d in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if is_valid(r,c,b,d):
                    board[r][c] = d
                    check_row[r].add(d)
                    check_col[c].add(d)
                    check_box[b].add(d)
                    if solve(q):
                        return True
                    # d is not possible for board[r][c], reset board[r][c]
                    board[r][c] = '.'
                    check_row[r].remove(d)
                    check_col[c].remove(d)
                    check_box[b].remove(d)
                    opt += 1    # valid option for heap sorting
            heapq.heappush(q, (opt, r,c))
            return False

        # put all empty cell in queue
        q = []
        for r in range(9):
            for c in range(9):
                b = r//3*3 + c//3
                # add empty cell to queue
                if board[r][c] == '.':
                    q.append((r,c))
                # add existing number to checks
                else:
                    check_row[r].add(board[r][c])
                    check_col[c].add(board[r][c])
                    check_box[b].add(board[r][c])
        # use heap to solve cell with least options first
        q = [(9 - len(check_row[r]|check_col[c]|check_box[b]), r,c) for r,c in q]
        heapq.heapify(q)
        solve(q)
        return board
    

# Time : Beats 54.45 %
# Memo : Beats 60.63 %
# Backtracking DFS with queue
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        check_row = [set() for x in range(9)]
        check_col = [set() for x in range(9)]
        check_box = [set() for x in range(9)]
        # only check validity for specific cell
        def is_valid(r,c,b,d):
            if d in check_row[r]: return False  # noqa: E701
            if d in check_col[c]: return False  # noqa: E701
            if d in check_box[b]: return False  # noqa: E701
            return True

        # pre-order dfs with backtracking
        def solve(q,n):
            # Return True if done
            if n==len(q):
                return True
            
            r,c = q[n]
            b = r//3*3 + c//3
            # d is possible for board[r][c], then guess next with board[r][c]=d
            for d in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if is_valid(r,c,b,d):
                    board[r][c] = d
                    check_row[r].add(d)
                    check_col[c].add(d)
                    check_box[b].add(d)
                    if solve(q,n+1):
                        return True
                    # d is not possible for board[r][c], reset board[r][c]
                    board[r][c] = '.'
                    check_row[r].remove(d)
                    check_col[c].remove(d)
                    check_box[b].remove(d)
            return False

        # put all empty cell in queue
        q = []
        for r in range(9):
            for c in range(9):
                # add empty cell to queue
                if board[r][c] == '.':
                    q.append((r,c))
                # add existing number to checks
                else:
                    check_row[r].add(board[r][c])
                    check_col[c].add(board[r][c])
                    check_box[r//3*3 + c//3].add(board[r][c])

        solve(q,0)
        return board
        