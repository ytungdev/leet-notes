from typing import List

# Time : Beats 100.0 %
# Memo : Beats 66.97 %
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag_max,area_max = 0,0
        for a,b in dimensions:
            # a*a faster than a**2
            diag = a*a + b*b
            area = a*b
            if diag > diag_max:
                diag_max = diag
                area_max = area
            elif diag == diag_max and area > area_max:
                area_max = area
        return area_max
        