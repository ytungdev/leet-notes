from typing import List

# Time : Beats 99.58 %
# Memo : Beats 33.33 %
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        for j in range(2):    
            if j==1:
                tops,bottoms = bottoms, tops
            res = 0
            alt = 1 if tops[0] != bottoms[0] else 0
            done = False
            for i in range(1,n):
                if tops[i] != tops[0]:
                    if bottoms[i] != tops[0]:
                        done = False
                        break
                    else:
                        res += 1
                elif bottoms[i] != tops[0]:
                    alt += 1
                done = True
            if done:                
                return min(alt,res)
        return -1