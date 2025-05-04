from typing import List
from collections import Counter

# Time : Beats 100.0 %
# Memo : Beats 43.37 %
## dict with id
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = {}
        res = 0
        for x,y in dominoes:
            id = x*10+y if x>y else y*10+x
            count = freq.get(id,0)
            res += count
            freq[id] = count+1
        return res

# Time : Beats 99.71 %
# Memo : Beats 17.97 %
## array with id
class Solution2:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = [0]*100
        res = 0
        for x,y in dominoes:
            id = x*10+y if x>y else y*10+x
            res += counter[id]
            counter[id] += 1
        return res


# Time : Beats 94.86 %
# Memo : Beats  7.56 %
## Count()
class Solution3:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = Counter([(x,y) if x<=y else (y,x) for x,y in dominoes])
        res = 0
        for d in counter:
            if counter[d] > 1:
                res += (counter[d]*((counter[d])-1))//2
        return res