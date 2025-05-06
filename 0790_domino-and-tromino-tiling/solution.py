from typing import List

# Time : Beats 100.0 %
# Memo : Beats 69.14 %
class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1,1,2,5,11]+[0]*(n-4)
        if n <5:
            return dp[n]
        
        for i in range(5,n+1):
            dp[i] = 2*dp[i-1]+dp[i-3]
        
        return dp[n]% (10**9+7)

# Time : Beats 66.81 %
# Memo : Beats 56.59 %
class Solution2:
    def numTilings(self, n: int) -> int:
        dp = [1,1,2,5]
        if n<=3:
            return dp[n]
        
        dp += [0]*(n-3)
        accum = [0]*(n+1)
        
        for i in range(3,n+1):
            accum[i-3] = accum[i-4] + dp[i-3]
            dp[i] = dp[i-1] + dp[i-2] + accum[i-3]*2
        return dp[n] % (10**9+7)