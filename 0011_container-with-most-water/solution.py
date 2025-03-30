from typing import List

# Time : Beats  5.21 %
# Memo : Beats 24.06 %

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        L,R = 0,len(height)-1
        while L<R:
            cur_vol = min(height[L], height[R]) * (R-L)
            max_vol = max(max_vol, cur_vol)
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1

        return max_vol
