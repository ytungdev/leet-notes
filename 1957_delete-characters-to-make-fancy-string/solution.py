from typing import List

# Time : Beats 98.61 %
# Memo : Beats 52.29 %
class Solution:
    def makeFancyString(self, s: str) -> str:
        '''
        - new char : add to ret, update prev and freq
        - same char : only add if freq < 2
        '''
        freq = 0
        prev = ''
        ret = ''
        for char in s:
            if char != prev:
                ret += char
                prev = char
                freq = 1
            elif freq < 2:
                ret += char
                freq += 1
        return ret