# Time : Beats 14.97 %
# Memo : Beats 99.97 %

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        res = 0
        seen = {}

        for R in range(len(s)):
            char = s[R]
            # repeated inside window, skipping L
            if seen.get(char,-1) >= L:
                L = seen[char]+1
            seen[char] = R
            res = max(res, R-L+1)

        return res