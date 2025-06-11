from typing import List
from collections import Counter

# Time : Beats 100.0 %
# Memo : Beats 22.94 %
class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        maxo=0
        mine=float('inf')
        for char,freq in counter.items():
            if freq%2 and freq > maxo:
                    maxo=freq
            if not freq%2 and freq < mine:
                    mine=freq
        return maxo-mine
        