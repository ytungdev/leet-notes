from typing import List

# Time : Beats 87.83 %
# Memo : Beats 80.92 %
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L'+dominoes+'R'
        dominoes = list(dominoes)
        n = len(dominoes)
        L,R = 0,1
        ret = []
        while R < n:
            if dominoes[R] == '.':
                R+=1
                continue
            if dominoes[R] != dominoes[L] and dominoes[R] == 'L':
                # R..L/R...L -> RRLL/RR.LL
                l,r = L,R
                while l<r:
                    dominoes[l] = 'R'
                    dominoes[r] = 'L'
                    l+=1
                    r-=1
                L=R
            elif dominoes[R] == dominoes[L]:
                # R..R/L..L -> RRRR or LLLL
                while L<R:
                    dominoes[L] = dominoes[R]
                    L+=1
            else:
                # L..R -> L..R
                L=R
            R+=1
        return ''.join(dominoes[1:-1])

# Time : Beats 16.12 %
# Memo : Beats 63.16 %
class Solution2:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0]*n
        # L - force
        curr_force = 0 
        for j in range(n-1,-1,-1):
            if dominoes[j] == 'L':
                curr_force = n
            elif dominoes[j] == 'R':
                curr_force = 0
            else:
                curr_force = max(0,curr_force-1)
            forces[j] -= curr_force
        # R- force
        curr_force = 0
        ret = ''
        for i in range(n):
            if dominoes[i] == 'R':
                curr_force = n
            elif dominoes[i] == 'L':
                curr_force = 0
            else:
                curr_force = max(0,curr_force-1)
            forces[i] += curr_force
        
            if forces[i] > 0:
                ret += 'R'
            elif forces[i] < 0:
                ret += 'L'
            else:
                ret += '.'

        return ret