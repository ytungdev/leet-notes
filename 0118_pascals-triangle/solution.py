from typing import List

# Time : Beats 100.0 %
# Memo : Beats 58.48 %
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            arr = []
            L = 0
            for R in res[-1]:
                arr.append(L+R)
                L=R
            arr.append(1)
            res.append(arr)
        return res
            
        