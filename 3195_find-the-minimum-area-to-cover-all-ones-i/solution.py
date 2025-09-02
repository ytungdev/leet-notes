from typing import List

# Time : Beats 93.26 %
# Memo : Beats 77.56 %
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        m = len(grid[0])
        n = len(grid)

        r_min,r_max = -1,-1
        c_min,c_max = -1,-1

        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    r_min = r
                    break
            if r_min != -1:
                break
        for r in range(n-1,-1,-1):
            for c in range(m):
                if grid[r][c]:
                    r_max = r
                    break
            if r_max != -1:
                break
        
        for c in range(m):
            for r in range(n):
                if grid[r][c]:
                    c_min = c
                    break
            if c_min != -1:
                break
        for c in range(m-1,-1,-1):
            for r in range(n):
                if grid[r][c]:
                    c_max = c
                    break
            if c_max != -1:
                break
        
        return (r_max-r_min+1)*(c_max-c_min+1)

# Time : Beats 76.18 %
# Memo : Beats 52.44 %
class Solution2:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        m = len(grid[0])
        n = len(grid)

        min_x, max_x = m,0
        min_y, max_y = n,0

        for y in range(n):
            for x in range(m):
                if grid[y][x]:
                    if x < min_x:
                        min_x = x
                    if x > max_x:
                        max_x = x
                    if y < min_y:
                        min_y = y
                    max_y = y

        return (max_x-min_x+1)*(max_y-min_y+1)