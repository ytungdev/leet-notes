from typing import List

# Time : Beats 86.90 %
# Memo : Beats 69.66 %
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        '''
        |ABC| = |U| - 3x|A'BC| + 3x|A'B'C| - |A'B'C'|
        '''
        def nC2(n):
            if n<2:
                return 0
            return (n-1)*n//2

        U = nC2(n+2)
        aBC = nC2(n-limit+1)
        abC = nC2(n-2*limit)
        abc = nC2(n-1-3*limit)
        return U-3*aBC+3*abC-abc
    
# Time : Beats 17.24 %
# Memo : Beats 93.10 %
class Solution2:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n>limit*3:
            return 0
        if n == limit*3:
            return 1
        res = 0
        for a in range(max(n-2*limit,0),min(limit,n)+1):
            res += min(n-a,limit)+1-max(0,n-limit-a)
        return res