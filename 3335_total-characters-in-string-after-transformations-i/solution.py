from typing import List
from collections import Counter

# Time : Beats 96.64 %
# Memo : Beats 18.79 %
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        dp = [1]*26 + [0]*t
        for i in range(26,t+26):
            dp[i] = (dp[i-26] + dp[i-25]) % mod
        
        res = 0
        # for char in s:
        #     res += dp[ord(char)-97 + t] % mod
        counter = Counter(s)
        for char,freq in counter.items():
            res += freq*dp[ord(char)-97 + t] % mod

        return res % mod


# Time : Beats 36.25 %
# Memo : Beats 91.28 %
class Solution2:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counter = [0]*26
        mod = 10**9 + 7
        for char in s:
            counter[ord(char)-97] += 1
        
        for j in range(t):
            temp = [0]*26
            # a-y
            for i in range(25):
                temp[i+1] = counter[i] % mod
            # z
            if counter[25]:
                temp[0] = counter[25] % mod
                temp[1] = (counter[25] + temp[1]) % mod
            counter = temp
        return sum(counter) % mod