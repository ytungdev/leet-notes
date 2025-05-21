from typing import List

# Time : Beats 100.0 %
# Memo : Beats 95.45 %
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        setRow0 = False
        # scan zeros
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r==0:
                        setRow0 = True
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
        # set zeros
        for r in range(m-1,0,-1):
            for c in range(n-1,-1,-1):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        # set row 0
        if setRow0:
            for c in range(n):
                matrix[0][c] = 0