from typing import List

# Time : Beats 81.39 %
# Memo : Beats 31.90 %
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ret = 0
        accum = 0
        L = 0
        for R in range(len(nums)):
            accum += nums[R]
            while L <= R and accum*(R-L+1) >= k:
                # shrink
                accum -= nums[L]
                L +=1
            ret += R-L+1
                
                
        return ret