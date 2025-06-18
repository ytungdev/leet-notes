from typing import List
import math

# Time : Beats  5.09 %
# Memo : Beats 54.43 %
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return m*math.comb(n-1,k)*(m-1)**(n-1-k) % (10**9+7)