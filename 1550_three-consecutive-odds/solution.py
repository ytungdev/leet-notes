from typing import List

# Time : Beats 100.0 %
# Memo : Beats 88.31 %
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0
        for num in arr:
            if num%2:
                odd+=1
                if odd==3:
                    return True
            else:
                odd = 0
        return False