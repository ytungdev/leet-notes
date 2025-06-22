from typing import List

# Time : Beats 100.0 %
# Memo : Beats 88.92 %
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        if n%k != 0:
            s = s + fill*(k - (n % k))
        
        n = len(s)
        ret = ['']*(n//k)
        for i in range(n):
            ret[i//k] += s[i]
            
        return ret   
    
# Time : Beats 100.0 %
# Memo : Beats 18.56 %
class Solution2:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        for i in range(0,len(s),k):
            ret.append(s[i:i+k])
        for j in range(k-len(ret[-1])):
            ret[-1] += fill
        return ret