from typing import List
from collections import Counter

# Time : Beats 94.51 %
# Memo : Beats 67.07 %
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word).values()
        
        # max freq when all char in word are the same
        res = len(word)
        for this_freq in freq:
            rm = 0
            for that_freq in freq:
                if this_freq == that_freq:
                    continue
                    
                if that_freq < this_freq:
                    # remove all
                    rm += that_freq
                elif that_freq > this_freq + k:
                    # remove extra
                    rm += that_freq - this_freq - k
                
            if rm < res:
                res = rm
        return res