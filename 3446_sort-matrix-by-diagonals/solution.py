from typing import List

# Time : Beats 89.14 %
# Memo : Beats 47.25 %
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        00 01 02
        10 11 12
        20 21 22

        c-r     layer
        2       0
        1       1
        0       2
        -1      3
        -2      4
        '''
        
        n = len(grid)
        layer = 2*n-1
        mid = layer//2
        
        # grid->nums
        nums = [[] for i in range(layer)]
        for r in range(n):
            for c in range(n):
                nums[n-1-c+r].append(grid[r][c])
        
        # sort
        for i in range(layer):
            if i >= mid:
                nums[i] = sorted(nums[i], reverse=True)
            else:
                nums[i] = sorted(nums[i])
            
        # nums->grid
        for r in range(n):
            for c in range(n):
                grid[r][c] = nums[n-1-c+r][min(r,c)]
        
        return grid


        