from typing import List

# Time : Beats 99.21 %
# Memo : Beats 21.21 %
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        ret = 0
        n = len(nums)
        
        pow2 = [1]
        for i in range(n):
            pow2.append(pow2[-1]*2%mod)

        L,R = 0,n-1
        while L<=R:
            if nums[L]+nums[R] <= target:
                # valid : add subsequence with min val nums[L] (2**(l-1))
                ret = (ret + pow2[R-L]) % mod
                L += 1
            else:
                R -= 1
        return ret
