from typing import List

# Time : Beats 96.50 %
# Memo : Beats 96.97 %
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = {i:i for i in 'abcdefghijklmnopqrstuvwxyz'}
        
        def find(char):
            # return root of char -- O(N)
            while char!=uf[char]:
                char = uf[char]
            return char
            
        n = len(s1)
        for i in range(n):
            r1 = find(s1[i])
            r2 = find(s2[i])
            if r1 <= r2:
                uf[r2] = r1
            else:
                uf[r1] = r2
        
        res=''
        for char in baseStr:
            res += find(char)
            
        return res