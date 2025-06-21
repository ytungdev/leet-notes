from typing import List

# Time : Beats 100.0 %
# Memo : Beats 69.85 %
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        '''
        calculate and compare distance with positive dir as:
        - N and E
        - N and W
        - S and E
        - S and W
        '''
        maxd = 0
        for pos in ['NE', 'NW', 'SE', 'SW']:
            quota = k
            dist = 0
            for d in s:
                if d in pos:
                    dist += 1
                elif quota > 0:
                    dist += 1
                    quota -= 1
                else:
                    dist -= 1
                if dist > maxd:
                    maxd = dist

        return maxd
    
# Time : Beats 87.50 %
# Memo : Beats 37.50 %
class Solution2:
    def maxDistance(self, s: str, k: int) -> int:
        c = {'N':0, 'E':0, 'S':0, 'W':0}
        ret = 0
        for i in range(len(s)):
            c[s[i]] += 1
            major = max(c['N'],c['S']) + max(c['E'],c['W'])
            minor = i+1 - major
            
            if minor > k:
                #d = major+k-(minor-k)
                d = major+2*k-minor
            else:
                #d = major+minor
                d = major+minor

            if d>ret:
                ret=d
        return ret