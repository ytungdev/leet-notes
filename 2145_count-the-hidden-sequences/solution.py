from typing import List

# Time : Beats 98.00 %
# Memo : Beats 12.00 %
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        accum = 0
        minp = 0
        maxp = 0
        # O(N)
        for diff in differences:
            accum += diff
            if accum > maxp:
                maxp = accum
            if accum < minp:
                minp = accum
        _min = lower - minp
        _max = upper - maxp
        if _max < _min:
            return 0
        return _max - _min + 1