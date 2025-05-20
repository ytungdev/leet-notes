from typing import List

# Time : Beats 75.42 %
# Memo : Beats 81.85 %
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9+7

        # generate all mask
        masks = []
        for i in range(3**m):
            this = []
            temp = i
            for j in range(m):
                this.append(temp%3)
                temp //=3
            if all([this[x] != this[x-1] for x in range(1,m)]):
                masks.append(this)
        k = len(masks)

        # generate all mask' for each mask
        maskn = []
        for mask1 in masks:
            possible = []
            for maski in range(k):
                if all([mask1[i] != masks[maski][i] for i in range(m)]):
                    possible.append(maski)
            maskn.append(possible)
        
        # calc f_i = [f[i][mask_0], .. , f[i][mask_k]] for each mask
        f_last = [1]*k
        for i in range(1,n):
            f_this = [0]*k
            for i in range(k):
                for j in maskn[i]:
                    f_this[i] += f_last[j]
                    if f_this[i] >= mod:
                        f_this[i] -= mod

            f_last = f_this
        return sum(f_last) % mod