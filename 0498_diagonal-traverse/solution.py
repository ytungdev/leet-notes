from typing import List

# Time : Beats 96.50 %
# Memo : Beats 27.47 %
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        ret = []
        lvl = 1
        r,c = 0,0
        for i in range(m*n):
            ret.append(mat[r][c])
            # odd level : UR
            if lvl % 2:
                # change direction, R -> D
                if r==0 or c==n-1:
                    lvl += 1
                    if c+1 < n:
                        c += 1
                    elif r+1 < m:
                        r += 1
                    else:
                        return ret
                # UR
                else:
                    r -= 1
                    c += 1
            # even level : DL
            else:
                # change direction, D -> R
                if c==0 or r==m-1:
                    lvl += 1
                    if r+1 < m:
                        r += 1
                    elif c+1 < n:
                        c += 1
                    else:
                        return ret
                # DL
                else:
                    r += 1
                    c -= 1

