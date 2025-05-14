from typing import List

# Time : Beats 49.62 %
# Memo : Beats 98.47 %
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9 + 7
        
        def mat_product(A,B):
            rowsA, colsA, colsB = len(A), len(A[0]), len(B[0])
            result = [[0]*colsB for _ in range(rowsA)]
            for i in range(rowsA):
                for j in range(colsB):
                    tmp = 0
                    for k in range(colsA):
                        tmp += A[i][k] * B[k][j]
                    result[i][j] = tmp % mod
            return result

        def expo_by_sq(mat, expo):
            # Identity matrix
            res = [[1 if i==j else 0 for j in range(26)] for i in range(26)]
            while expo > 0:
                if expo & 1:
                    res = mat_product(res, mat)
                mat = mat_product(mat, mat)
                expo >>= 1
            return res
        # transformation matrix T(i,j)
        # = 1 if j is included in i-transformation, 
        # else 0
        T = [[0]*26 for _ in range(26)]
        for i in range(26):
            for j in range(1,nums[i]+1):
                T[i][(i+j)%26] = 1
       
        freq = [[0]*26]
        for char in s:
            freq[0][ord(char) - 97] += 1
        
        res = mat_product(freq, expo_by_sq(T, t))
        return sum(res[0]) % mod