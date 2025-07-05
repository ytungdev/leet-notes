from typing import List
from collections import Counter

# Time : Beats 100.0 %
# Memo : Beats 17.79 %
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        ret = -1
        for i in c:
            if i==c[i] and i > ret:
                ret = i
        return ret