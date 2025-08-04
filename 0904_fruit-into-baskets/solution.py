from typing import List

# Time : Beats 99.63 %
# Memo : Beats 76.92 %
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        b1 = fruits[0]  # curr
        b2 = -1         # alt
        L = 0
        M = 0
        ret = 1
        for R in range(1,n):
            if fruits[R] == b1:
                continue
            if b2 == -1:
                b2 = fruits[R]

            if fruits[R] == b2:
                M = R
                b1,b2 = b2,b1
            else:
                ret = max(ret, R-L)
                b1, b2 = fruits[R], b1
                L = M
                M = R
        return max(ret, n-L)











