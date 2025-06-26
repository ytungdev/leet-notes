from typing import List

# Time : Beats 100.0 %
# Memo : Beats 66.91 %
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        c = 0
        place_val = 1
        accum_val = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                c += 1
            elif place_val + accum_val <= k:
                accum_val += place_val
                c += 1
            else:
                break
            place_val *= 2
        for j in s[:i]:
            if j == '0':
                c += 1
        return c